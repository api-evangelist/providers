---
aid: amazon-web-services-aws
url: https://raw.githubusercontent.com/api-evangelist/amazon-web-services-aws/refs/heads/main/apis.yml
apis:
- name: Amazon EC2 API
  description: Amazon Elastic Compute Cloud (EC2) provides scalable computing capacity in the AWS cloud.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/ec2/
  baseURL: https://ec2.amazonaws.com
  tags:
  - Compute
  - Instances
  - Virtual Machines
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/ec2/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ec2/2016-11-15/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/ec2/pricing/
  - type: Console
    url: https://console.aws.amazon.com/ec2/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
  - type: FAQ
    url: https://aws.amazon.com/ec2/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-ec2
- name: Amazon S3 API
  description: Amazon Simple Storage Service is storage for the Internet designed to make web-scale computing easier.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/s3/
  baseURL: https://s3.amazonaws.com
  tags:
  - Cloud Storage
  - Object Storage
  - Storage
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/s3/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/s3/2006-03-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/s3/pricing/
  - type: Console
    url: https://console.aws.amazon.com/s3/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html
  - type: FAQ
    url: https://aws.amazon.com/s3/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-s3
- name: Amazon Lambda API
  description: AWS Lambda lets you run code without provisioning or managing servers.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/lambda/
  baseURL: https://lambda.amazonaws.com
  tags:
  - Compute
  - Functions
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lambda/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/lambda/2015-03-31/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/lambda/pricing/
  - type: Console
    url: https://console.aws.amazon.com/lambda/
  - type: Getting Started
    url: https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/lambda/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-lambda
- name: Amazon RDS API
  description: Amazon Relational Database Service makes it easy to set up, operate, and scale a relational database in the cloud.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/rds/
  baseURL: https://rds.amazonaws.com
  tags:
  - Database
  - MySQL
  - PostgreSQL
  - Relational Database
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/rds/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/rds/2014-10-31/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/rds/pricing/
  - type: Console
    url: https://console.aws.amazon.com/rds/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html
  - type: FAQ
    url: https://aws.amazon.com/rds/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-rds
- name: Amazon DynamoDB API
  description: Amazon DynamoDB is a fast and flexible NoSQL database service for applications that need consistent, single-digit millisecond latency.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/dynamodb/
  baseURL: https://dynamodb.amazonaws.com
  tags:
  - Database
  - Key-Value Store
  - NoSQL
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/dynamodb/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/dynamodb/2012-08-10/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/dynamodb/pricing/
  - type: Console
    url: https://console.aws.amazon.com/dynamodb/
  - type: Getting Started
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html
  - type: FAQ
    url: https://aws.amazon.com/dynamodb/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-dynamodb
- name: Amazon API Gateway API
  description: Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/api-gateway/
  baseURL: https://apigateway.amazonaws.com
  tags:
  - API Gateway
  - API Management
  - REST APIs
  - WebSocket
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/apigateway/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/apigateway/2015-07-09/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/api-gateway/pricing/
  - type: Console
    url: https://console.aws.amazon.com/apigateway/
  - type: Getting Started
    url: https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/api-gateway/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-api-gateway
- name: Amazon SQS API
  description: Amazon Simple Queue Service is a fully managed message queuing service for decoupling and scaling microservices, distributed systems, and serverless applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/sqs/
  baseURL: https://sqs.amazonaws.com
  tags:
  - Messaging
  - Microservices
  - Queues
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/sqs/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/sqs/2012-11-05/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/sqs/pricing/
  - type: Console
    url: https://console.aws.amazon.com/sqs/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/sqs/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-sqs
- name: Amazon SNS API
  description: Amazon Simple Notification Service is a fully managed pub/sub messaging service for application-to-application and application-to-person communication.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/sns/
  baseURL: https://sns.amazonaws.com
  tags:
  - Messaging
  - Notifications
  - Pub/Sub
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/sns/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/sns/2010-03-31/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/sns/pricing/
  - type: Console
    url: https://console.aws.amazon.com/sns/
  - type: Getting Started
    url: https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/sns/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-sns
- name: AWS CloudFormation API
  description: AWS CloudFormation provides infrastructure as code to model, provision, and manage AWS and third-party resources by treating infrastructure as code.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudformation/
  baseURL: https://cloudformation.amazonaws.com
  tags:
  - DevOps
  - Infrastructure as Code
  - Provisioning
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cloudformation/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/cloudformation/2010-05-15/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/cloudformation/pricing/
  - type: Console
    url: https://console.aws.amazon.com/cloudformation/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html
  - type: FAQ
    url: https://aws.amazon.com/cloudformation/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-cloudformation
- name: AWS IAM API
  description: AWS Identity and Access Management enables you to securely manage identities and access to AWS services and resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/iam/
  baseURL: https://iam.amazonaws.com
  tags:
  - Access Management
  - Authentication
  - Identity
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/iam/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/iam/2010-05-08/openapi.yaml
  - type: Console
    url: https://console.aws.amazon.com/iam/
  - type: Getting Started
    url: https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/iam/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-iam
- name: Amazon ECS API
  description: Amazon Elastic Container Service is a fully managed container orchestration service that helps you deploy, manage, and scale containerized applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/ecs/
  baseURL: https://ecs.amazonaws.com
  tags:
  - Containers
  - Docker
  - Orchestration
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/ecs/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ecs/2014-11-13/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/ecs/pricing/
  - type: Console
    url: https://console.aws.amazon.com/ecs/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/ecs/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-ecs
- name: Amazon EKS API
  description: Amazon Elastic Kubernetes Service is a managed Kubernetes service that makes it easy to run Kubernetes on AWS and on-premises.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/eks/
  baseURL: https://eks.amazonaws.com
  tags:
  - Containers
  - Kubernetes
  - Orchestration
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/eks/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/eks/2017-11-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/eks/pricing/
  - type: Console
    url: https://console.aws.amazon.com/eks/
  - type: Getting Started
    url: https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/eks/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-eks
- name: Amazon CloudWatch API
  description: Amazon CloudWatch is an observability service that provides monitoring and operational data in the form of logs, metrics, and events for AWS resources and applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudwatch/
  baseURL: https://monitoring.amazonaws.com
  tags:
  - Logging
  - Metrics
  - Monitoring
  - Observability
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cloudwatch/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/monitoring/2010-08-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/cloudwatch/pricing/
  - type: Console
    url: https://console.aws.amazon.com/cloudwatch/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingStarted.html
  - type: FAQ
    url: https://aws.amazon.com/cloudwatch/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-cloudwatch
- name: Amazon Kinesis API
  description: Amazon Kinesis makes it easy to collect, process, and analyze real-time streaming data so you can get timely insights and react quickly to new information.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/kinesis/
  baseURL: https://kinesis.amazonaws.com
  tags:
  - Analytics
  - Data Processing
  - Real-Time
  - Streaming
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/kinesis/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/kinesis/2013-12-02/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/kinesis/data-streams/pricing/
  - type: Console
    url: https://console.aws.amazon.com/kinesis/
  - type: Getting Started
    url: https://docs.aws.amazon.com/streams/latest/dev/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/kinesis/data-streams/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-kinesis
- name: Amazon CloudFront API
  description: Amazon CloudFront is a fast content delivery network service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudfront/
  baseURL: https://cloudfront.amazonaws.com
  tags:
  - Caching
  - CDN
  - Content Delivery
  - Edge Computing
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cloudfront/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/cloudfront/2020-05-31/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/cloudfront/pricing/
  - type: Console
    url: https://console.aws.amazon.com/cloudfront/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html
  - type: FAQ
    url: https://aws.amazon.com/cloudfront/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-cloudfront
- name: Amazon Route 53 API
  description: Amazon Route 53 is a highly available and scalable Domain Name System web service for reliable and cost-effective domain routing.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/route53/
  baseURL: https://route53.amazonaws.com
  tags:
  - DNS
  - Domain Names
  - Networking
  - Traffic Routing
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/route53/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/route53/2013-04-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/route53/pricing/
  - type: Console
    url: https://console.aws.amazon.com/route53/
  - type: Getting Started
    url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/route53/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-route-53
- name: Amazon Cognito API
  description: Amazon Cognito provides customer identity and access management enabling secure sign-in and access control for web and mobile applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cognito/
  baseURL: https://cognito-idp.amazonaws.com
  tags:
  - Authentication
  - Authorization
  - Identity
  - User Management
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cognito/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/cognito-idp/2016-04-18/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/cognito/pricing/
  - type: Console
    url: https://console.aws.amazon.com/cognito/
  - type: Getting Started
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/cognito/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-cognito
- name: AWS Step Functions API
  description: AWS Step Functions is a serverless orchestration service that lets you build visual workflows to coordinate distributed applications and microservices.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/step-functions/
  baseURL: https://states.amazonaws.com
  tags:
  - Orchestration
  - Serverless
  - State Machines
  - Workflows
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/step-functions/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/states/2016-11-23/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/step-functions/pricing/
  - type: Console
    url: https://console.aws.amazon.com/states/
  - type: Getting Started
    url: https://docs.aws.amazon.com/step-functions/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/step-functions/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-step-functions
- name: Amazon SageMaker API
  description: Amazon SageMaker is a fully managed service that provides the ability to build, train, and deploy machine learning models at scale.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/sagemaker/
  baseURL: https://api.sagemaker.amazonaws.com
  tags:
  - Artificial Intelligence
  - Data Science
  - Machine Learning
  - Model Training
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/sagemaker/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/sagemaker/2017-07-24/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/sagemaker/pricing/
  - type: Console
    url: https://console.aws.amazon.com/sagemaker/
  - type: Getting Started
    url: https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html
  - type: FAQ
    url: https://aws.amazon.com/sagemaker/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-sagemaker
- name: Amazon Bedrock API
  description: Amazon Bedrock is a fully managed service that provides access to foundation models from leading AI companies for building generative AI applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/bedrock/
  baseURL: https://bedrock.amazonaws.com
  tags:
  - Artificial Intelligence
  - Foundation Models
  - Generative AI
  - Large Language Models
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/bedrock/
  - type: Pricing
    url: https://aws.amazon.com/bedrock/pricing/
  - type: Console
    url: https://console.aws.amazon.com/bedrock/
  - type: Getting Started
    url: https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/bedrock/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-bedrock
- name: Amazon EventBridge API
  description: Amazon EventBridge is a serverless event bus service that makes it easy to connect applications using data from your own applications, SaaS applications, and AWS services.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/eventbridge/
  baseURL: https://events.amazonaws.com
  tags:
  - Event-Driven
  - Events
  - Integration
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/eventbridge/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/eventbridge/2015-10-07/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/eventbridge/pricing/
  - type: Console
    url: https://console.aws.amazon.com/events/
  - type: Getting Started
    url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html
  - type: FAQ
    url: https://aws.amazon.com/eventbridge/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-eventbridge
- name: Elastic Load Balancing API
  description: Elastic Load Balancing automatically distributes incoming application traffic across multiple targets and virtual appliances in one or more Availability Zones.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/elasticloadbalancing/
  baseURL: https://elasticloadbalancing.amazonaws.com
  tags:
  - High Availability
  - Load Balancing
  - Networking
  - Traffic Distribution
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/elasticloadbalancing/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/elasticloadbalancingv2/2015-12-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/elasticloadbalancing/pricing/
  - type: Console
    url: https://console.aws.amazon.com/ec2/home#LoadBalancers
  - type: Getting Started
    url: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html
  - type: FAQ
    url: https://aws.amazon.com/elasticloadbalancing/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-elastic-load-balancing
- name: Amazon VPC API
  description: Amazon Virtual Private Cloud lets you define and launch AWS resources in a logically isolated virtual network with full control over your networking environment.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/vpc/
  baseURL: https://ec2.amazonaws.com
  tags:
  - Isolation
  - Networking
  - Security
  - Virtual Private Cloud
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/vpc/
  - type: Pricing
    url: https://aws.amazon.com/vpc/pricing/
  - type: Console
    url: https://console.aws.amazon.com/vpc/
  - type: Getting Started
    url: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/vpc/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-vpc
- name: AWS Secrets Manager API
  description: AWS Secrets Manager helps you centrally manage the lifecycle of secrets including database credentials, API keys, and other secrets used throughout your applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/secrets-manager/
  baseURL: https://secretsmanager.amazonaws.com
  tags:
  - Credentials
  - Key Management
  - Secrets
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/secretsmanager/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/secretsmanager/2017-10-17/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/secrets-manager/pricing/
  - type: Console
    url: https://console.aws.amazon.com/secretsmanager/
  - type: Getting Started
    url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/secrets-manager/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-secrets-manager
- name: Amazon Athena API
  description: Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon S3 using standard SQL.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/athena/
  baseURL: https://athena.amazonaws.com
  tags:
  - Analytics
  - Data Lake
  - Query
  - SQL
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/athena/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/athena/2017-05-18/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/athena/pricing/
  - type: Console
    url: https://console.aws.amazon.com/athena/
  - type: Getting Started
    url: https://docs.aws.amazon.com/athena/latest/ug/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/athena/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-athena
- name: Amazon Aurora API
  description: Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/rds/aurora/
  baseURL: https://rds.amazonaws.com
  tags:
  - Database
  - MySQL
  - PostgreSQL
  - Relational Database
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/
  - type: Pricing
    url: https://aws.amazon.com/rds/aurora/pricing/
  - type: Console
    url: https://console.aws.amazon.com/rds/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.html
  - type: FAQ
    url: https://aws.amazon.com/rds/aurora/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-aurora
- name: Amazon AppFlow API
  description: Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between SaaS applications and AWS services.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/appflow/
  baseURL: https://appflow.amazonaws.com
  tags:
  - Data Transfer
  - ETL
  - Integration
  - SaaS
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/appflow/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/appflow/2020-08-23/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/appflow/pricing/
  - type: Console
    url: https://console.aws.amazon.com/appflow/
  - type: Getting Started
    url: https://docs.aws.amazon.com/appflow/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/appflow/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-appflow
- name: AWS AppSync API
  description: AWS AppSync creates serverless GraphQL and Pub/Sub APIs that simplify application development through a single endpoint for data querying, updating, and publishing.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/appsync/
  baseURL: https://appsync.amazonaws.com
  tags:
  - GraphQL
  - Real-Time
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/appsync/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/appsync/2017-07-25/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/appsync/pricing/
  - type: Console
    url: https://console.aws.amazon.com/appsync/
  - type: Getting Started
    url: https://docs.aws.amazon.com/appsync/latest/devguide/welcome.html
  - type: FAQ
    url: https://aws.amazon.com/appsync/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-appsync
- name: AWS App Runner API
  description: AWS App Runner is a fully managed container application service that makes it easy to quickly deploy from source code or a container image directly to a scalable and secure web application.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/apprunner/
  baseURL: https://apprunner.amazonaws.com
  tags:
  - Containers
  - Deployment
  - Serverless
  - Web Applications
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/apprunner/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/apprunner/2020-05-15/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/apprunner/pricing/
  - type: Console
    url: https://console.aws.amazon.com/apprunner/
  - type: Getting Started
    url: https://docs.aws.amazon.com/apprunner/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/apprunner/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-app-runner
- name: AWS Batch API
  description: AWS Batch enables developers to easily and efficiently run hundreds of thousands of batch computing jobs on AWS.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/batch/
  baseURL: https://batch.amazonaws.com
  tags:
  - Batch Computing
  - Compute
  - HPC
  - Job Scheduling
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/batch/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/batch/2016-08-10/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/batch/pricing/
  - type: Console
    url: https://console.aws.amazon.com/batch/
  - type: Getting Started
    url: https://docs.aws.amazon.com/batch/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/batch/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-batch
- name: AWS Backup API
  description: AWS Backup is a fully managed backup service that makes it easy to centralize and automate the backup of data across AWS services.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/backup/
  baseURL: https://backup.amazonaws.com
  tags:
  - Backup
  - Data Protection
  - Disaster Recovery
  - Storage
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/aws-backup/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/backup/2018-11-15/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/backup/pricing/
  - type: Console
    url: https://console.aws.amazon.com/backup/
  - type: Getting Started
    url: https://docs.aws.amazon.com/aws-backup/latest/devguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/backup/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-backup
- name: AWS Certificate Manager API
  description: AWS Certificate Manager lets you easily provision, manage, and deploy public and private SSL/TLS certificates for use with AWS services and your internal connected resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/certificate-manager/
  baseURL: https://acm.amazonaws.com
  tags:
  - Certificates
  - Security
  - SSL
  - TLS
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/acm/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/acm/2015-12-08/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/certificate-manager/pricing/
  - type: Console
    url: https://console.aws.amazon.com/acm/
  - type: Getting Started
    url: https://docs.aws.amazon.com/acm/latest/userguide/gs.html
  - type: FAQ
    url: https://aws.amazon.com/certificate-manager/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-certificate-manager
- name: AWS CloudTrail API
  description: AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account by logging API calls.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudtrail/
  baseURL: https://cloudtrail.amazonaws.com
  tags:
  - Audit
  - Compliance
  - Governance
  - Logging
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cloudtrail/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/cloudtrail/2013-11-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/cloudtrail/pricing/
  - type: Console
    url: https://console.aws.amazon.com/cloudtrail/
  - type: Getting Started
    url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/cloudtrail/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-cloudtrail
- name: Amazon CloudSearch API
  description: Amazon CloudSearch is a managed service in the AWS Cloud that makes it simple and cost-effective to set up, manage, and scale a search solution for your website or application.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudsearch/
  baseURL: https://cloudsearch.amazonaws.com
  tags:
  - Full-Text Search
  - Indexing
  - Search
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cloudsearch/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/cloudsearch/2013-01-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/cloudsearch/pricing/
  - type: Console
    url: https://console.aws.amazon.com/cloudsearch/
  - type: Getting Started
    url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/cloudsearch/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-cloudsearch
- name: AWS CodeBuild API
  description: AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/codebuild/
  baseURL: https://codebuild.amazonaws.com
  tags:
  - Build
  - CI/CD
  - Continuous Integration
  - DevOps
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/codebuild/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/codebuild/2016-10-06/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/codebuild/pricing/
  - type: Console
    url: https://console.aws.amazon.com/codebuild/
  - type: Getting Started
    url: https://docs.aws.amazon.com/codebuild/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/codebuild/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-codebuild
- name: AWS CodeDeploy API
  description: AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services such as EC2, Fargate, Lambda, and on-premises servers.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/codedeploy/
  baseURL: https://codedeploy.amazonaws.com
  tags:
  - Automation
  - CI/CD
  - Deployment
  - DevOps
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/codedeploy/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/codedeploy/2014-10-06/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/codedeploy/pricing/
  - type: Console
    url: https://console.aws.amazon.com/codedeploy/
  - type: Getting Started
    url: https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/codedeploy/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-codedeploy
- name: AWS CodePipeline API
  description: AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/codepipeline/
  baseURL: https://codepipeline.amazonaws.com
  tags:
  - CI/CD
  - Continuous Delivery
  - DevOps
  - Pipeline
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/codepipeline/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/codepipeline/2015-07-09/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/codepipeline/pricing/
  - type: Console
    url: https://console.aws.amazon.com/codepipeline/
  - type: Getting Started
    url: https://docs.aws.amazon.com/codepipeline/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/codepipeline/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-codepipeline
- name: Amazon Comprehend API
  description: Amazon Comprehend is a natural language processing service that uses machine learning to find insights and relationships in text.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/comprehend/
  baseURL: https://comprehend.amazonaws.com
  tags:
  - AI
  - Machine Learning
  - NLP
  - Text Analysis
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/comprehend/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/comprehend/2017-11-27/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/comprehend/pricing/
  - type: Console
    url: https://console.aws.amazon.com/comprehend/
  - type: Getting Started
    url: https://docs.aws.amazon.com/comprehend/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/comprehend/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-comprehend
- name: AWS Config API
  description: AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources for compliance and security.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/config/
  baseURL: https://config.amazonaws.com
  tags:
  - Audit
  - Compliance
  - Configuration
  - Governance
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/config/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/config/2014-11-12/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/config/pricing/
  - type: Console
    url: https://console.aws.amazon.com/config/
  - type: Getting Started
    url: https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/config/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-config
- name: Amazon Connect API
  description: Amazon Connect is a cloud-based contact center service that makes it easy to deliver customer service at any scale with omnichannel communications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/connect/
  baseURL: https://connect.amazonaws.com
  tags:
  - Contact Center
  - Customer Service
  - Omnichannel
  - Telephony
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/connect/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/connect/2017-08-08/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/connect/pricing/
  - type: Console
    url: https://console.aws.amazon.com/connect/
  - type: Getting Started
    url: https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html
  - type: FAQ
    url: https://aws.amazon.com/connect/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-connect
- name: AWS Database Migration Service API
  description: AWS Database Migration Service helps you migrate databases to AWS quickly and securely while the source database remains fully operational during the migration.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/dms/
  baseURL: https://dms.amazonaws.com
  tags:
  - Data Transfer
  - Database
  - Migration
  - Replication
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/dms/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/dms/2016-01-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/dms/pricing/
  - type: Console
    url: https://console.aws.amazon.com/dms/
  - type: Getting Started
    url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html
  - type: FAQ
    url: https://aws.amazon.com/dms/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-dms
- name: AWS Direct Connect API
  description: AWS Direct Connect is a cloud service that links your network directly to AWS to deliver consistent, low-latency performance.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/directconnect/
  baseURL: https://directconnect.amazonaws.com
  tags:
  - Dedicated Connection
  - Hybrid Cloud
  - Networking
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/directconnect/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/directconnect/2012-10-25/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/directconnect/pricing/
  - type: Console
    url: https://console.aws.amazon.com/directconnect/
  - type: Getting Started
    url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/getting_started.html
  - type: FAQ
    url: https://aws.amazon.com/directconnect/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-direct-connect
- name: Amazon DocumentDB API
  description: Amazon DocumentDB is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/documentdb/
  baseURL: https://rds.amazonaws.com
  tags:
  - Database
  - Document Database
  - MongoDB
  - NoSQL
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/documentdb/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/docdb/2014-10-31/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/documentdb/pricing/
  - type: Console
    url: https://console.aws.amazon.com/docdb/
  - type: Getting Started
    url: https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html
  - type: FAQ
    url: https://aws.amazon.com/documentdb/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-documentdb
- name: Amazon ECR API
  description: Amazon Elastic Container Registry is a fully managed container registry offering high-performance hosting so you can reliably deploy application images and artifacts anywhere.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/ecr/
  baseURL: https://api.ecr.amazonaws.com
  tags:
  - Container Registry
  - Containers
  - Docker
  - Images
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/ecr/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ecr/2015-09-21/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/ecr/pricing/
  - type: Console
    url: https://console.aws.amazon.com/ecr/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html
  - type: FAQ
    url: https://aws.amazon.com/ecr/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-ecr
- name: Amazon EBS API
  description: Amazon Elastic Block Store provides persistent block storage volumes for use with Amazon EC2 instances in the AWS Cloud.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/ebs/
  baseURL: https://ec2.amazonaws.com
  tags:
  - Block Storage
  - Snapshots
  - Storage
  - Volumes
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/ebs/
  - type: Pricing
    url: https://aws.amazon.com/ebs/pricing/
  - type: Console
    url: https://console.aws.amazon.com/ec2/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html
  - type: FAQ
    url: https://aws.amazon.com/ebs/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-ebs
- name: Amazon EFS API
  description: Amazon Elastic File System provides a simple, serverless, elastic file system that lets you share file data without provisioning or managing storage.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/efs/
  baseURL: https://elasticfilesystem.amazonaws.com
  tags:
  - File Storage
  - NFS
  - Shared Storage
  - Storage
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/efs/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/elasticfilesystem/2015-02-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/efs/pricing/
  - type: Console
    url: https://console.aws.amazon.com/efs/
  - type: Getting Started
    url: https://docs.aws.amazon.com/efs/latest/ug/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/efs/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-efs
- name: Amazon ElastiCache API
  description: Amazon ElastiCache is a fully managed in-memory caching service supporting Redis and Memcached for real-time applications requiring sub-millisecond latency.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/elasticache/
  baseURL: https://elasticache.amazonaws.com
  tags:
  - Caching
  - In-Memory
  - Memcached
  - Redis
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/elasticache/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/elasticache/2015-02-02/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/elasticache/pricing/
  - type: Console
    url: https://console.aws.amazon.com/elasticache/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/elasticache/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-elasticache
- name: AWS Elastic Beanstalk API
  description: AWS Elastic Beanstalk is a service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/elasticbeanstalk/
  baseURL: https://elasticbeanstalk.amazonaws.com
  tags:
  - Compute
  - Deployment
  - PaaS
  - Web Applications
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/elasticbeanstalk/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/elasticbeanstalk/2010-12-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/elasticbeanstalk/pricing/
  - type: Console
    url: https://console.aws.amazon.com/elasticbeanstalk/
  - type: Getting Started
    url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html
  - type: FAQ
    url: https://aws.amazon.com/elasticbeanstalk/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-elastic-beanstalk
- name: Amazon EMR API
  description: Amazon EMR is a cloud big data platform for processing vast amounts of data using open source tools such as Apache Spark, Hive, HBase, Flink, and Presto.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/emr/
  baseURL: https://elasticmapreduce.amazonaws.com
  tags:
  - Analytics
  - Big Data
  - Hadoop
  - Spark
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/emr/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/elasticmapreduce/2009-03-31/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/emr/pricing/
  - type: Console
    url: https://console.aws.amazon.com/emr/
  - type: Getting Started
    url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html
  - type: FAQ
    url: https://aws.amazon.com/emr/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-emr
- name: AWS Fargate API
  description: AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS removing the need to manage servers.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/fargate/
  baseURL: https://ecs.amazonaws.com
  tags:
  - Compute
  - Containers
  - Docker
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html
  - type: Pricing
    url: https://aws.amazon.com/fargate/pricing/
  - type: Console
    url: https://console.aws.amazon.com/ecs/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonECS/latest/userguide/getting-started-fargate.html
  - type: FAQ
    url: https://aws.amazon.com/fargate/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-fargate
- name: Amazon FSx API
  description: Amazon FSx provides fully managed third-party file systems with the native compatibility and feature sets for workloads including Windows, Lustre, NetApp ONTAP, and OpenZFS.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/fsx/
  baseURL: https://fsx.amazonaws.com
  tags:
  - File System
  - Lustre
  - Storage
  - Windows
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/fsx/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/fsx/2018-03-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/fsx/pricing/
  - type: Console
    url: https://console.aws.amazon.com/fsx/
  - type: Getting Started
    url: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/fsx/windows/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-fsx
- name: AWS Global Accelerator API
  description: AWS Global Accelerator is a networking service that improves the availability and performance of your applications with users globally using the AWS global network.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/global-accelerator/
  baseURL: https://globalaccelerator.amazonaws.com
  tags:
  - Availability
  - Global
  - Networking
  - Performance
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/global-accelerator/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/globalaccelerator/2018-08-08/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/global-accelerator/pricing/
  - type: Console
    url: https://console.aws.amazon.com/globalaccelerator/
  - type: Getting Started
    url: https://docs.aws.amazon.com/global-accelerator/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/global-accelerator/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-global-accelerator
- name: AWS Glue API
  description: AWS Glue is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/glue/
  baseURL: https://glue.amazonaws.com
  tags:
  - Analytics
  - Data Catalog
  - Data Integration
  - ETL
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/glue/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/glue/2017-03-31/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/glue/pricing/
  - type: Console
    url: https://console.aws.amazon.com/glue/
  - type: Getting Started
    url: https://docs.aws.amazon.com/glue/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/glue/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-glue
- name: Amazon GuardDuty API
  description: Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/guardduty/
  baseURL: https://guardduty.amazonaws.com
  tags:
  - Compliance
  - Monitoring
  - Security
  - Threat Detection
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/guardduty/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/guardduty/2017-11-28/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/guardduty/pricing/
  - type: Console
    url: https://console.aws.amazon.com/guardduty/
  - type: Getting Started
    url: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html
  - type: FAQ
    url: https://aws.amazon.com/guardduty/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-guardduty
- name: Amazon Inspector API
  description: Amazon Inspector is an automated vulnerability management service that continually scans AWS workloads for software vulnerabilities and unintended network exposure.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/inspector/
  baseURL: https://inspector2.amazonaws.com
  tags:
  - Compliance
  - Scanning
  - Security
  - Vulnerability
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/inspector/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/inspector2/2020-06-08/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/inspector/pricing/
  - type: Console
    url: https://console.aws.amazon.com/inspector/
  - type: Getting Started
    url: https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html
  - type: FAQ
    url: https://aws.amazon.com/inspector/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-inspector
- name: AWS IoT Core API
  description: AWS IoT Core lets connected devices easily and securely interact with cloud applications and other devices using MQTT, HTTPS, and LoRaWAN protocols.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/iot-core/
  baseURL: https://iot.amazonaws.com
  tags:
  - Device Management
  - Internet of Things
  - IoT
  - MQTT
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/iot/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/iot/2015-05-28/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/iot-core/pricing/
  - type: Console
    url: https://console.aws.amazon.com/iot/
  - type: Getting Started
    url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html
  - type: FAQ
    url: https://aws.amazon.com/iot-core/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-iot-core
- name: Amazon Kendra API
  description: Amazon Kendra is an intelligent search service powered by machine learning that enables you to search across different content repositories with built-in connectors.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/kendra/
  baseURL: https://kendra.amazonaws.com
  tags:
  - AI
  - Enterprise Search
  - Machine Learning
  - Search
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/kendra/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/kendra/2019-02-03/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/kendra/pricing/
  - type: Console
    url: https://console.aws.amazon.com/kendra/
  - type: Getting Started
    url: https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/kendra/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-kendra
- name: Amazon Keyspaces API
  description: Amazon Keyspaces is a scalable, highly available, and managed Apache Cassandra-compatible database service for running Cassandra workloads in the cloud.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/keyspaces/
  baseURL: https://cassandra.amazonaws.com
  tags:
  - Cassandra
  - Database
  - NoSQL
  - Wide Column
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/keyspaces/
  - type: Pricing
    url: https://aws.amazon.com/keyspaces/pricing/
  - type: Console
    url: https://console.aws.amazon.com/keyspaces/
  - type: Getting Started
    url: https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/keyspaces/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-keyspaces
- name: AWS KMS API
  description: AWS Key Management Service makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/kms/
  baseURL: https://kms.amazonaws.com
  tags:
  - Cryptography
  - Encryption
  - Key Management
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/kms/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/kms/2014-11-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/kms/pricing/
  - type: Console
    url: https://console.aws.amazon.com/kms/
  - type: Getting Started
    url: https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/kms/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-kms
- name: AWS Lake Formation API
  description: AWS Lake Formation is a service that makes it easy to set up a secure data lake in days by simplifying and automating data ingestion, cataloging, transformation, and security.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/lake-formation/
  baseURL: https://lakeformation.amazonaws.com
  tags:
  - Analytics
  - Data Governance
  - Data Lake
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lake-formation/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/lakeformation/2017-03-31/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/lake-formation/pricing/
  - type: Console
    url: https://console.aws.amazon.com/lakeformation/
  - type: Getting Started
    url: https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-tutorial.html
  - type: FAQ
    url: https://aws.amazon.com/lake-formation/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-lakeformation
- name: Amazon Lex API
  description: Amazon Lex is a service for building conversational interfaces into any application using voice and text, powered by the same technology as Amazon Alexa.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/lex/
  baseURL: https://models-v2-lex.amazonaws.com
  tags:
  - Chatbot
  - Conversational AI
  - NLP
  - Voice
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lex/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/models.lex.v2/2020-08-07/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/lex/pricing/
  - type: Console
    url: https://console.aws.amazon.com/lexv2/
  - type: Getting Started
    url: https://docs.aws.amazon.com/lexv2/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/lex/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-lex
- name: Amazon Lightsail API
  description: Amazon Lightsail offers easy-to-use virtual private server instances, containers, storage, databases, and more at a cost-effective monthly price.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/lightsail/
  baseURL: https://lightsail.amazonaws.com
  tags:
  - Compute
  - Simple Cloud
  - VPS
  - Web Hosting
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lightsail/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/lightsail/2016-11-28/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/lightsail/pricing/
  - type: Console
    url: https://lightsail.aws.amazon.com/
  - type: Getting Started
    url: https://docs.aws.amazon.com/lightsail/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/lightsail/faq/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-lightsail
- name: Amazon Macie API
  description: Amazon Macie is a data security service that discovers sensitive data using machine learning and pattern matching and provides visibility into data security risks.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/macie/
  baseURL: https://macie2.amazonaws.com
  tags:
  - Compliance
  - Data Privacy
  - Machine Learning
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/macie/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/macie2/2020-01-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/macie/pricing/
  - type: Console
    url: https://console.aws.amazon.com/macie/
  - type: Getting Started
    url: https://docs.aws.amazon.com/macie/latest/user/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/macie/faq/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-macie
- name: Amazon MemoryDB API
  description: Amazon MemoryDB is a Redis-compatible, durable, in-memory database service that delivers ultra-fast performance for modern applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/memorydb/
  baseURL: https://memory-db.amazonaws.com
  tags:
  - Caching
  - Database
  - In-Memory
  - Redis
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/memorydb/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/memorydb/2021-01-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/memorydb/pricing/
  - type: Console
    url: https://console.aws.amazon.com/memorydb/
  - type: Getting Started
    url: https://docs.aws.amazon.com/memorydb/latest/devguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/memorydb/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-memorydb
- name: Amazon MQ API
  description: Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/amazon-mq/
  baseURL: https://mq.amazonaws.com
  tags:
  - ActiveMQ
  - Message Broker
  - Messaging
  - RabbitMQ
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/amazon-mq/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/mq/2017-11-27/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/amazon-mq/pricing/
  - type: Console
    url: https://console.aws.amazon.com/amazon-mq/
  - type: Getting Started
    url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/amazon-mq/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-mq
- name: Amazon MSK API
  description: Amazon Managed Streaming for Apache Kafka is a fully managed service that makes it easy to build and run applications that use Apache Kafka to process streaming data.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/msk/
  baseURL: https://kafka.amazonaws.com
  tags:
  - Apache Kafka
  - Event Streaming
  - Real-Time
  - Streaming
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/msk/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/kafka/2018-11-14/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/msk/pricing/
  - type: Console
    url: https://console.aws.amazon.com/msk/
  - type: Getting Started
    url: https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/msk/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-msk
- name: Amazon OpenSearch Service API
  description: Amazon OpenSearch Service makes it easy to deploy, operate, and scale OpenSearch clusters for log analytics, full-text search, application monitoring, and more.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/opensearch-service/
  baseURL: https://es.amazonaws.com
  tags:
  - Analytics
  - Log Analytics
  - OpenSearch
  - Search
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/opensearch-service/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/opensearch/2021-01-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/opensearch-service/pricing/
  - type: Console
    url: https://console.aws.amazon.com/aos/
  - type: Getting Started
    url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html
  - type: FAQ
    url: https://aws.amazon.com/opensearch-service/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-opensearch
- name: AWS Organizations API
  description: AWS Organizations helps you centrally manage and govern your environment as you grow and scale your AWS resources across multiple accounts.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/organizations/
  baseURL: https://organizations.amazonaws.com
  tags:
  - Governance
  - Management
  - Multi-Account
  - Policy
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/organizations/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/organizations/2016-11-28/openapi.yaml
  - type: Console
    url: https://console.aws.amazon.com/organizations/
  - type: Getting Started
    url: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/organizations/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-organizations
- name: Amazon Personalize API
  description: Amazon Personalize enables developers to build applications with the same machine learning technology used by Amazon.com for real-time personalized recommendations.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/personalize/
  baseURL: https://personalize.amazonaws.com
  tags:
  - AI
  - Machine Learning
  - Personalization
  - Recommendations
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/personalize/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/personalize/2018-05-22/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/personalize/pricing/
  - type: Console
    url: https://console.aws.amazon.com/personalize/
  - type: Getting Started
    url: https://docs.aws.amazon.com/personalize/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/personalize/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-personalize
- name: Amazon Pinpoint API
  description: Amazon Pinpoint is a flexible and scalable outbound and inbound marketing communications service for engaging customers across multiple channels.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/pinpoint/
  baseURL: https://pinpoint.amazonaws.com
  tags:
  - Email
  - Marketing
  - Messaging
  - Push Notifications
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/pinpoint/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/pinpoint/2016-12-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/pinpoint/pricing/
  - type: Console
    url: https://console.aws.amazon.com/pinpoint/
  - type: Getting Started
    url: https://docs.aws.amazon.com/pinpoint/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/pinpoint/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-pinpoint
- name: Amazon Polly API
  description: Amazon Polly is a service that turns text into lifelike speech, allowing you to create applications that talk and build entirely new categories of speech-enabled products.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/polly/
  baseURL: https://polly.amazonaws.com
  tags:
  - AI
  - Speech Synthesis
  - Text-To-Speech
  - Voice
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/polly/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/polly/2016-06-10/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/polly/pricing/
  - type: Console
    url: https://console.aws.amazon.com/polly/
  - type: Getting Started
    url: https://docs.aws.amazon.com/polly/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/polly/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-polly
- name: Amazon QuickSight API
  description: Amazon QuickSight is a fast, cloud-powered business intelligence service that makes it easy to deliver insights and visualizations to everyone in your organization.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/quicksight/
  baseURL: https://quicksight.amazonaws.com
  tags:
  - Analytics
  - Business Intelligence
  - Dashboards
  - Visualization
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/quicksight/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/quicksight/2018-04-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/quicksight/pricing/
  - type: Console
    url: https://quicksight.aws.amazon.com/
  - type: Getting Started
    url: https://docs.aws.amazon.com/quicksight/latest/user/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/quicksight/resources/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-q
- name: Amazon Rekognition API
  description: Amazon Rekognition offers pre-trained and customizable computer vision capabilities to extract information and insights from your images and videos.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/rekognition/
  baseURL: https://rekognition.amazonaws.com
  tags:
  - AI
  - Computer Vision
  - Image Analysis
  - Video Analysis
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/rekognition/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/rekognition/2016-06-27/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/rekognition/pricing/
  - type: Console
    url: https://console.aws.amazon.com/rekognition/
  - type: Getting Started
    url: https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/rekognition/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-rekognition
- name: Amazon SES API
  description: Amazon Simple Email Service is a cost-effective, flexible, and scalable email service that enables you to send and receive email using your own email addresses and domains.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/ses/
  baseURL: https://email.amazonaws.com
  tags:
  - Email
  - Marketing
  - Messaging
  - Transactional Email
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/ses/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/sesv2/2019-09-27/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/ses/pricing/
  - type: Console
    url: https://console.aws.amazon.com/ses/
  - type: Getting Started
    url: https://docs.aws.amazon.com/ses/latest/dg/setting-up.html
  - type: FAQ
    url: https://aws.amazon.com/ses/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-ses
- name: AWS Security Hub API
  description: AWS Security Hub is a cloud security posture management service that performs security best practice checks, aggregates alerts, and enables automated remediation.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/security-hub/
  baseURL: https://securityhub.amazonaws.com
  tags:
  - Compliance
  - CSPM
  - Monitoring
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/securityhub/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/securityhub/2018-10-26/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/security-hub/pricing/
  - type: Console
    url: https://console.aws.amazon.com/securityhub/
  - type: Getting Started
    url: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html
  - type: FAQ
    url: https://aws.amazon.com/security-hub/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-security-hub
- name: AWS Systems Manager API
  description: AWS Systems Manager is a management service that helps you automatically collect software inventory, apply OS patches, create system images, and configure Windows and Linux operating systems.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/systems-manager/
  baseURL: https://ssm.amazonaws.com
  tags:
  - Automation
  - Management
  - Operations
  - Patching
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/systems-manager/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ssm/2014-11-06/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/systems-manager/pricing/
  - type: Console
    url: https://console.aws.amazon.com/systems-manager/
  - type: Getting Started
    url: https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/systems-manager/faq/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-systems-manager
- name: Amazon Textract API
  description: Amazon Textract is a machine learning service that automatically extracts text, handwriting, and data from scanned documents.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/textract/
  baseURL: https://textract.amazonaws.com
  tags:
  - AI
  - Document Processing
  - Machine Learning
  - OCR
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/textract/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/textract/2018-06-27/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/textract/pricing/
  - type: Console
    url: https://console.aws.amazon.com/textract/
  - type: Getting Started
    url: https://docs.aws.amazon.com/textract/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/textract/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-textract
- name: Amazon Timestream API
  description: Amazon Timestream is a fast, scalable, and serverless time series database service for IoT and operational applications that can store and analyze trillions of events per day.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/timestream/
  baseURL: https://ingest.timestream.amazonaws.com
  tags:
  - Analytics
  - Database
  - IoT
  - Time Series
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/timestream/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/timestream-write/2018-11-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/timestream/pricing/
  - type: Console
    url: https://console.aws.amazon.com/timestream/
  - type: Getting Started
    url: https://docs.aws.amazon.com/timestream/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/timestream/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-timestream
- name: Amazon Transcribe API
  description: Amazon Transcribe is an automatic speech recognition service that makes it easy to add speech-to-text capability to your applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/transcribe/
  baseURL: https://transcribe.amazonaws.com
  tags:
  - AI
  - Machine Learning
  - Speech-To-Text
  - Transcription
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/transcribe/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/transcribe/2017-10-26/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/transcribe/pricing/
  - type: Console
    url: https://console.aws.amazon.com/transcribe/
  - type: Getting Started
    url: https://docs.aws.amazon.com/transcribe/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/transcribe/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-transcribe
- name: Amazon Translate API
  description: Amazon Translate is a neural machine translation service that delivers fast, high-quality, affordable, and customizable language translation.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/translate/
  baseURL: https://translate.amazonaws.com
  tags:
  - AI
  - Localization
  - NLP
  - Translation
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/translate/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/translate/2017-07-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/translate/pricing/
  - type: Console
    url: https://console.aws.amazon.com/translate/
  - type: Getting Started
    url: https://docs.aws.amazon.com/translate/latest/dg/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/translate/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-translate
- name: AWS Transit Gateway API
  description: AWS Transit Gateway connects VPCs and on-premises networks through a central hub simplifying your network and putting an end to complex peering relationships.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/transit-gateway/
  baseURL: https://ec2.amazonaws.com
  tags:
  - Hybrid Cloud
  - Networking
  - Transit
  - VPC
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/vpc/latest/tgw/
  - type: Pricing
    url: https://aws.amazon.com/transit-gateway/pricing/
  - type: Console
    url: https://console.aws.amazon.com/vpc/
  - type: Getting Started
    url: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/transit-gateway/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-transit-gateway
- name: AWS WAF API
  description: AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits and bots that may affect availability or security.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/waf/
  baseURL: https://wafv2.amazonaws.com
  tags:
  - DDoS Protection
  - Firewall
  - Security
  - Web Application Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/waf/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/wafv2/2019-07-29/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/waf/pricing/
  - type: Console
    url: https://console.aws.amazon.com/wafv2/
  - type: Getting Started
    url: https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/waf/faq/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-waf
- name: AWS X-Ray API
  description: AWS X-Ray helps developers analyze and debug production and distributed applications such as those built using a microservices architecture.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/xray/
  baseURL: https://xray.amazonaws.com
  tags:
  - Debugging
  - Monitoring
  - Observability
  - Tracing
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/xray/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/xray/2016-04-12/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/xray/pricing/
  - type: Console
    url: https://console.aws.amazon.com/xray/
  - type: Getting Started
    url: https://docs.aws.amazon.com/xray/latest/devguide/xray-gettingstarted.html
  - type: FAQ
    url: https://aws.amazon.com/xray/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-xray
- name: Amazon Location Service API
  description: Amazon Location Service makes it easy for developers to add location functionality to applications without compromising data security and user privacy.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/location/
  baseURL: https://geo.amazonaws.com
  tags:
  - Geofencing
  - Location
  - Maps
  - Routing
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/location/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/location/2020-11-19/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/location/pricing/
  - type: Console
    url: https://console.aws.amazon.com/location/
  - type: Getting Started
    url: https://docs.aws.amazon.com/location/latest/developerguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/location/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-location-service
- name: AWS Amplify API
  description: AWS Amplify is a set of tools and features that enables frontend web and mobile developers to quickly and easily build full-stack applications on AWS.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/amplify/
  baseURL: https://amplify.amazonaws.com
  tags:
  - Frontend
  - Full-Stack
  - Mobile
  - Web Development
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/amplify/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/amplify/2017-07-25/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/amplify/pricing/
  - type: Console
    url: https://console.aws.amazon.com/amplify/
  - type: Getting Started
    url: https://docs.aws.amazon.com/amplify/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/amplify/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-amplify
- name: AWS Storage Gateway API
  description: AWS Storage Gateway is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/storagegateway/
  baseURL: https://storagegateway.amazonaws.com
  tags:
  - Backup
  - Gateway
  - Hybrid Cloud
  - Storage
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/storagegateway/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/storagegateway/2013-06-30/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/storagegateway/pricing/
  - type: Console
    url: https://console.aws.amazon.com/storagegateway/
  - type: Getting Started
    url: https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStarted.html
  - type: FAQ
    url: https://aws.amazon.com/storagegateway/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-storage-gateway
- name: AWS DataSync API
  description: AWS DataSync is an online data movement and discovery service that simplifies and accelerates data migration to and between AWS storage services.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/datasync/
  baseURL: https://datasync.amazonaws.com
  tags:
  - Data Transfer
  - Migration
  - Storage
  - Sync
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/datasync/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/datasync/2018-11-09/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/datasync/pricing/
  - type: Console
    url: https://console.aws.amazon.com/datasync/
  - type: Getting Started
    url: https://docs.aws.amazon.com/datasync/latest/userguide/getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/datasync/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-datasync
- name: Amazon S3 Glacier API
  description: Amazon S3 Glacier and S3 Glacier Deep Archive are secure, durable, and extremely low-cost cloud storage classes for data archiving and long-term backup.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/s3/storage-classes/glacier/
  baseURL: https://glacier.amazonaws.com
  tags:
  - Archive
  - Backup
  - Cold Storage
  - Storage
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/amazonglacier/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/glacier/2012-06-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/s3/pricing/
  - type: Console
    url: https://console.aws.amazon.com/glacier/
  - type: Getting Started
    url: https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-getting-started.html
  - type: FAQ
    url: https://aws.amazon.com/s3/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-s3
- name: AWS Shield API
  description: AWS Shield is a managed DDoS protection service that safeguards applications running on AWS with always-on detection and automatic inline mitigations.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/shield/
  baseURL: https://shield.amazonaws.com
  tags:
  - DDoS Protection
  - Networking
  - Protection
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/shield/2016-06-02/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/shield/pricing/
  - type: Console
    url: https://console.aws.amazon.com/wafv2/
  - type: Getting Started
    url: https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html
  - type: FAQ
    url: https://aws.amazon.com/shield/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-shield
- name: Amazon Detective API
  description: Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/detective/
  baseURL: https://api.detective.amazonaws.com
  tags:
  - Forensics
  - Investigation
  - Security
  - Threat Analysis
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/detective/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/detective/2018-10-26/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/detective/pricing/
  - type: Console
    url: https://console.aws.amazon.com/detective/
  - type: Getting Started
    url: https://docs.aws.amazon.com/detective/latest/userguide/detective-setup.html
  - type: FAQ
    url: https://aws.amazon.com/detective/faqs/
  - type: GitRepository
    url: https://github.com/api-evangelist/amazon-detective
name: Amazon Web Services (AWS)
tags:
- Analytics
- Artificial Intelligence
- Cloud Computing
- Computing
- Containers
- Databases
- DevOps
- IaaS
- Infrastructure
- Machine Learning
- Networking
- PaaS
- Platform as a Service
- Security
- Serverless
- Storage
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Web Services offers reliable, scalable, and inexpensive cloud computing services. Free to join, pay only for what you use.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

