from pathlib import Path
from invoke import task, Collection

prod = Collection("prod")
dev = Collection("dev")
namespace = Collection(prod, dev)


@task
def clean(ctx):
    with ctx.cd("infrastructure"):
        ctx.run(
            "make clean",
            env={"ENV_NAME": ctx.ENV_NAME, "AWS_REGION": ctx.AWS_REGION},
        )


@task
def build(ctx, clean=False):
    with ctx.cd("infrastructure"):
        if clean:
            ctx.run(
                "make clean",
                env={"ENV_NAME": ctx.ENV_NAME, "AWS_REGION": ctx.AWS_REGION},
            )

        ctx.run(
            "make build-template",
            env={"ENV_NAME": ctx.ENV_NAME, "AWS_REGION": ctx.AWS_REGION},
        )


@task
def deploy(ctx, clean=False):
    with ctx.cd("infrastructure"):
        if clean:
            ctx.run(
                "make clean",
                env={"ENV_NAME": ctx.ENV_NAME, "AWS_REGION": ctx.AWS_REGION},
            )

        ctx.run(
            "make deploy-template",
            env={"ENV_NAME": ctx.ENV_NAME, "AWS_REGION": ctx.AWS_REGION},
        )


for invoke_task in (build, deploy, clean):
    prod.add_task(invoke_task)
    dev.add_task(invoke_task)

prod.configure({"ENV_NAME": "aw2-prod"})
dev.configure({"ENV_NAME": "aw2-dev"})
namespace.configure({"AWS_REGION": "ap-southeast-2"})
