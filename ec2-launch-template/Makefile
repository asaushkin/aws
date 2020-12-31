
STACK_NAME ?= GenericEC2InstanceProfile

ifdef AWS_REGION
	SOURCE_REGION ?= $(AWS_REGION)
else
	SOURCE_REGION ?= eu-central-1
endif

CLOUDFORMATION_TEMPLATE := ec2-launch-template.yaml

ARTIFACT_BUCKET := eu-central-1-268700153966
ARTIFACT_PREFIX := cloudformation-deploy

all:
	@echo ++ $(SOURCE_REGION) ++
	@echo "****************************************************************************************"
	@echo "Create Generic EC2 profile with a command"
	@echo
	@echo "  make create_app"
	@echo
	@echo "You can customize the run command with the next options"
	@echo
	@echo "  STACK_NAME=MyStackName SOURCE_REGION=us-west-2 make create_app"
	@echo
	@echo "There're next commands for the make: create_app, update_app, delete_app"
	@echo "****************************************************************************************"


create_app:
	aws cloudformation --region $(SOURCE_REGION) deploy --stack-name $(STACK_NAME) \
		--capabilities CAPABILITY_IAM  \
		--template-file ./$(CLOUDFORMATION_TEMPLATE)
		--s3-bucket $(ARTIFACT_BUCKET) --s3-prefix $(ARTIFACT_PREFIX)

	#aws cloudformation --region $(SOURCE_REGION) wait stack-create-complete --stack-name $(STACK_NAME)
	#aws cloudformation --region $(SOURCE_REGION) describe-stacks --stack-name $(STACK_NAME)

update_app:
	aws cloudformation --region $(SOURCE_REGION) update-stack --stack-name $(STACK_NAME) \
		--capabilities CAPABILITY_IAM   \
		--template-body file://./$(CLOUDFORMATION_TEMPLATE)

	aws cloudformation --region $(SOURCE_REGION) wait stack-update-complete --stack-name $(STACK_NAME)
	aws cloudformation --region $(SOURCE_REGION) describe-stacks --stack-name $(STACK_NAME)

delete_app:
	aws cloudformation --region $(SOURCE_REGION) delete-stack --stack-name $(STACK_NAME)
	aws cloudformation --region $(SOURCE_REGION) wait stack-delete-complete --stack-name $(STACK_NAME)

