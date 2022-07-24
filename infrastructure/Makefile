ifndef ENV_NAME
$(error ENV_NAME is undefined)
endif
ifndef AWS_REGION
$(error AWS_REGION is undefined)
endif

IN_FILES := $(wildcard *.yaml.in) $(wildcard */*.yaml.in)
GENERATED_FILES := $(patsubst %.yaml.in,%.yaml,$(IN_FILES))

.PHONY: deploy
deploy-%: build-%
	$(info Deploying with AWS SAM...)
	@cd ..; sam deploy \
		--config-env $(ENV_NAME) \
		--region $(AWS_REGION) \
		--parameter-overrides \
			EnvironmentName=$(ENV_NAME)

.PHONY: build
build-%: %.yaml $(GENERATED_FILES)
	$(info Building $< with AWS SAM...)
	@sam validate \
		--template $<

	@sam build \
		--template $< \
		--build-dir ../.aws-sam/build

%.yaml: %.yaml.in
	$(info Generating ${@}...)
	@gpp -x $< | yq -P > $@

clean:
	$(info Cleaning...)
	@rm -rf $(GENERATED_FILES)
