---
aid: aws-lambda
url: https://raw.githubusercontent.com/api-evangelist/aws-lambda/refs/heads/main/apis.yml
apis:
- name: AWS Lambda API
  description: The AWS Lambda REST API enables you to create, manage, and invoke Lambda functions programmatically. Supports function management, event source mappings, aliases, versions, and layer operations.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://aws.amazon.com/lambda/
  baseUrl: https://lambda.{region}.amazonaws.com
  tags:
  - Compute
  - Event-Driven
  - Faas
  - Functions
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/lambda/2015-03-31/openapi.json
  - type: OpenAPI
    url: openapi/aws-lambda-api-openapi.yml
  - type: AsyncAPI
    url: asyncapi/aws-lambda-event-triggers-asyncapi.yml
  - type: JSONSchema
    url: json-schema/aws-lambda-function-schema.json
  - type: JSON-LD
    url: json-ld/aws-lambda-context.jsonld
  - type: API-Reference
    url: https://docs.aws.amazon.com/lambda/latest/api/welcome.html
  - type: Pricing
    url: https://aws.amazon.com/lambda/pricing/
  - type: Getting-Started
    url: https://aws.amazon.com/lambda/getting-started/
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Console
    url: https://console.aws.amazon.com/lambda/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Limits
    url: https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html
  - type: Best-Practices
    url: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
  - type: Security
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html
  - type: Tutorials
    url: https://aws.amazon.com/lambda/resources/
  - type: API-Actions
    url: https://docs.aws.amazon.com/lambda/latest/api/API_Operations.html
  - type: CLI-Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/lambda/
  - type: Permissions
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html
  - type: Execution-Role
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html
  - type: Monitoring
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html
  - type: Logging
    url: https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html
  - type: Versioning
    url: https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html
  - type: Environment-Variables
    url: https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
  - type: Concurrency
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html
  - type: Provisioned-Concurrency
    url: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html
  - type: Layers
    url: https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html
  - type: Function-URLs
    url: https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html
  - type: SnapStart
    url: https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html
  - type: Extensions
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html
  - type: Troubleshooting
    url: https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-deployment.html
  - type: Code-Examples
    url: https://docs.aws.amazon.com/lambda/latest/dg/service_code_examples.html
  - type: Configuration
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html
  - type: IAM-Authorization
    url: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslambda.html
  contact:
  - type: Support
    url: https://aws.amazon.com/contact-us/
  - type: Twitter
    url: https://twitter.com/awscloud
  - type: Forum
    url: https://repost.aws/tags/TA5uNafDy2TpGNjidWLMSxDw/aws-lambda
- name: AWS Lambda Extensions API
  description: The Lambda Extensions API enables you to create extensions that integrate with the Lambda execution environment lifecycle. Extensions can run as companion processes alongside your function, enabling use cases such as capturing diagnostic information, sending telemetry data, and integrating with monitoring and observability tools.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html
  baseUrl: https://lambda.{region}.amazonaws.com
  tags:
  - Extensions
  - Monitoring
  - Observability
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html
  - type: API-Reference
    url: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-extensions-api.html
  - type: Partners
    url: https://docs.aws.amazon.com/lambda/latest/dg/extensions-api-partners.html
  - type: Code-Examples
    url: https://github.com/aws-samples/aws-lambda-extensions
  - type: Configuration
    url: https://docs.aws.amazon.com/lambda/latest/dg/extensions-configuration.html
  contact:
  - type: Support
    url: https://aws.amazon.com/contact-us/
- name: AWS Lambda Telemetry API
  description: The Lambda Telemetry API lets you collect telemetry data directly from the Lambda execution environment. Extensions can subscribe to telemetry streams for platform telemetry, function logs, and extension logs to send data to custom destinations for monitoring and observability.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html
  baseUrl: https://lambda.{region}.amazonaws.com
  tags:
  - Logging
  - Monitoring
  - Observability
  - Serverless
  - Telemetry
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html
  - type: API-Reference
    url: https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api-reference.html
  - type: Schema-Reference
    url: https://docs.aws.amazon.com/lambda/latest/dg/telemetry-schema-reference.html
  contact:
  - type: Support
    url: https://aws.amazon.com/contact-us/
- name: AWS Lambda Runtime API
  description: The Lambda Runtime API enables you to use custom runtimes to run functions in any programming language. The runtime API provides an HTTP API for custom runtimes to receive invocation events from Lambda and send response data back within the Lambda execution environment.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html
  baseUrl: https://lambda.{region}.amazonaws.com
  tags:
  - Custom-Runtime
  - Functions
  - Runtime
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
  - type: API-Reference
    url: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html
  - type: Execution-Environment
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html
  contact:
  - type: Support
    url: https://aws.amazon.com/contact-us/
- name: AWS Lambda Logs API
  description: The Lambda Logs API enables extensions to subscribe to log streams generated by the Lambda platform, function code, and extensions within the execution environment, providing access to log data for processing and forwarding.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-logs-api.html
  baseUrl: https://lambda.{region}.amazonaws.com
  tags:
  - Logging
  - Monitoring
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-logs-api.html
  - type: Monitoring
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html
  contact:
  - type: Support
    url: https://aws.amazon.com/contact-us/
name: AWS Lambda
tags:
- API
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. Lambda runs your code on high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

