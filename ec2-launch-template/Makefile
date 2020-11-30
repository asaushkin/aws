
STACK_NAME ?= EC2InstanceProfile

create_stack: package
	aws cloudformation create-stack --stack-name $(STACK_NAME) \
		--parameters \
        	ParameterKey=CodeBucket,ParameterValue=$(S3_ARTIFACTS_BUCKET) \
		--capabilities CAPABILITY_IAM --capabilities CAPABILITY_NAMED_IAM  \
		--template-body file://./template.yaml --disable-rollback
	aws cloudformation wait stack-create-complete --stack-name $(STACK_NAME)
	aws cloudformation describe-stacks --stack-name $(STACK_NAME)

update_stack: package
	aws cloudformation update-stack --stack-name $(STACK_NAME) \
		--parameters \
        	ParameterKey=CodeBucket,ParameterValue=$(S3_ARTIFACTS_BUCKET) \
		--capabilities CAPABILITY_IAM --capabilities CAPABILITY_NAMED_IAM  \
		--template-body file://./template.yaml
	aws cloudformation wait stack-update-complete --stack-name $(STACK_NAME)
	aws cloudformation describe-stacks --stack-name $(STACK_NAME)

delete_stack:
	aws cloudformation delete-stack --stack-name $(STACK_NAME)
	aws cloudformation wait stack-delete-complete --stack-name $(STACK_NAME)

describe_stack:
	aws cloudformation describe-stacks --stack-name $(STACK_NAME)

update_lambda: package
	aws lambda update-function-code --function-name \
		$$(aws cloudformation describe-stacks --stack-name $(STACK_NAME) | \
			jq -r '.Stacks[0].Outputs[] | \
			select(.OutputKey == "ConfigRuleFunction") | \
			.OutputValue') \
		--zip-file fileb://open_ingress_config_rule.zip
	aws lambda update-function-code --function-name \
		$$(aws cloudformation describe-stacks --stack-name $(STACK_NAME) | \
			jq -r '.Stacks[0].Outputs[] | \
			select(.OutputKey == "RemediationFunction") | \
			.OutputValue') \
		--zip-file fileb://open_ingress_config_rule.zip
