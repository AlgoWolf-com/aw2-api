# pylint: disable=redefined-outer-name,line-too-long
from invoke import task, Collection

global_col = Collection("global")
prod = Collection("prod")
staging = Collection("staging")
dev = Collection("dev")
namespace = Collection(global_col, prod, staging, dev)


@task
def build(ctx, template):
    ctx.run("sam build " f"--template {template} " "--build-dir .aws-sam/build ")


@task
def deploy(ctx, feature_name=""):
    stack_name = f"{ctx.ENV_NAME}"
    env_name = ctx.ENV_NAME
    if ctx.COLLECTION_NAME == "dev":
        if not feature_name:
            raise AssertionError("dev environment must have feature_name")
        stack_name += f"-{feature_name}"
        env_name = f"{env_name}-{feature_name}".lower()
        repository_branch = feature_name
    else:
        if feature_name:
            raise AssertionError("Only dev environment can have feature_name")
        if ctx.COLLECTION_NAME == "prod":
            repository_branch = "production"
        elif ctx.COLLECTION_NAME == "staging":
            repository_branch = "master"

    global_deploy(ctx)
    build(ctx, "infrastructure/template.yaml")
    ctx.run(
        "sam deploy "
        f"--stack-name {stack_name} "
        "--s3-bucket aws-sam-$(aws sts get-caller-identity --no-cli-pager --query Account --output text) "
        f"--s3-prefix {stack_name} "
        f"--region {ctx.AWS_REGION} "
        "--no-confirm-changeset "
        "--no-fail-on-empty-changeset "
        "--capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND "
        "--parameter-overrides "
        f'ParameterKey="EnvironmentName",ParameterValue="{env_name}" '
        f'ParameterKey="RepositoryBranch",ParameterValue="{repository_branch}" '
        "--resolve-image-repos "
    )


@task
def dependencies_deploy(ctx, feature_name=""):
    stack_name = f"{ctx.ENV_NAME}-dependencies"
    env_name = ctx.ENV_NAME
    if ctx.COLLECTION_NAME == "dev":
        if not feature_name:
            raise AssertionError("dev environment must have feature_name")
        stack_name += f"-{feature_name}"
        env_name = f"{env_name}-{feature_name}".lower()
        repository_branch = feature_name
    else:
        if feature_name:
            raise AssertionError("Only dev environment can have feature_name")
        if ctx.COLLECTION_NAME == "prod":
            repository_branch = "production"
        elif ctx.COLLECTION_NAME == "staging":
            repository_branch = "master"

    global_deploy(ctx)
    build(ctx, "infrastructure/dependencies-template.yaml")
    ctx.run(
        "sam deploy "
        f"--stack-name {stack_name} "
        "--s3-bucket aws-sam-$(aws sts get-caller-identity --no-cli-pager --query Account --output text) "
        f"--s3-prefix {stack_name} "
        f"--region {ctx.AWS_REGION} "
        "--no-confirm-changeset "
        "--no-fail-on-empty-changeset "
        "--capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND "
        "--parameter-overrides "
        f'ParameterKey="EnvironmentName",ParameterValue="{env_name}" '
        f'ParameterKey="RepositoryBranch",ParameterValue="{repository_branch}" '
        "--resolve-image-repos "
    )


@task
def global_deploy(ctx):
    build(ctx, "infrastructure/global-template.yaml")
    ctx.run(
        "sam deploy "
        f"--stack-name aw2-global "
        "--s3-bucket aws-sam-$(aws sts get-caller-identity --no-cli-pager --query Account --output text) "
        f"--s3-prefix aw2-global "
        f"--region {ctx.AWS_REGION} "
        "--no-confirm-changeset "
        "--no-fail-on-empty-changeset "
        "--capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND "
        "--resolve-image-repos "
    )


@task
def create_env(ctx, feature_name=""):
    dependencies_deploy(ctx, feature_name=feature_name)


for invoke_task in (build, deploy, dependencies_deploy, create_env):
    prod.add_task(invoke_task)
    staging.add_task(invoke_task)
    dev.add_task(invoke_task)
global_col.add_task(global_deploy)

global_col.configure({"COLLECTION_NAME": "global", "ENV_NAME": "aw2-global"})
prod.configure({"COLLECTION_NAME": "prod", "ENV_NAME": "aw2-prod"})
staging.configure({"COLLECTION_NAME": "staging", "ENV_NAME": "aw2-staging"})
dev.configure({"COLLECTION_NAME": "dev", "ENV_NAME": "aw2-dev"})
namespace.configure({"AWS_REGION": "ap-southeast-2"})
