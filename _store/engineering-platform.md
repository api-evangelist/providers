---
aid: apis-io-engineering-platform
name: APIs.io Engineering Platform
type: Platform
position: Producer
access: Internal
description: This is an index of all of the infrastructure and services used to operate the engineering side of APIs.io, providing a single manifest of all the 3rd-party suppliers we depend on for digital resources and capabilities.The goal of this engineering platform definition is to define the platform in a way that can be federated and distributed as part of API operations, helping educate teams where they can access platform resources.
tags:
  - APIs.io
  - Engineering
  - Platform
created: '2024-09-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apis-io-engineering-platform:aws-s3
    name: Amazon S3
    description: Amazon S3 is used for centralized object storage, managing all images, video, and audio across sites via public and private buckets.
    humanURL: https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html
    baseURL: https://{bucketname}.s3.amazonaws.com
    tags:
      - Cloud
      - Storage
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/aws-s3-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-1ab188a6-cc1f-490d-9413-9c6da20918d0?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-0e94f581-cbc1-48e0-b594-1f6b3d07a328?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-4517d93a-e7f7-4dc2-b572-06762bbe14de?action=share&creator=35240
  - aid: apis-io-engineering-platform:aws-lambda
    name: AWS Lambda
    description: AWS Lambda is an event-driven, serverless Function as a Service provided by Amazon as a part of Amazon Web Services.
    humanURL: https://docs.aws.amazon.com/lambda/
    baseURL: https://r275xc9bmd.execute-api.us-east-1.amazonaws.com
    tags:
      - Compute
      - Execute
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lambda/latest/api/welcome.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/aws-lambda-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-88f9ddbb-3115-47dc-b6e5-7fc6f1d2a190?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-3a12caae-4945-4df4-8ab9-bb6219ba7a9f?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-863b18f0-c2f2-4e32-a5fa-0d1e6ccf77a9?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-189876d1-f207-49a2-a4bc-5c67ae78cd19?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-c1e74fd9-3f84-4d95-943d-d645d6cb82f7?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-b002164d-6e8a-4b6d-b409-4929476e7818?action=share&creator=35240
  - aid: apis-io-engineering-platform:aws-api-gateway
    name: AWS API Gateway
    description: Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
    humanURL: https://aws.amazon.com/api-gateway/
    baseURL: http://api.example.com
    tags:
      - Gateway
    properties:
      - type: Documentation
        url: https://example.com/documentation
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/aws-api-gateway-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-508660fd-30b8-4c9c-aede-8edbac8a514d?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-da35e0ba-f1a9-42fe-a77a-56ff0a47e341?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-1d4df7d0-9c92-4fa8-946f-2110c2b3b48d?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-2af6f54f-d259-46c0-8f86-78856f5885cd?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-cc203f31-e7f6-42ec-ad34-c5c4cde58904?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-f19285da-48dd-4691-bbdf-f7d6bec157a3?action=share&creator=35240
  - aid: apis-io-engineering-platform:aws-rds
    name: AWS RDS
    description: Amazon Relational Database Service (Amazon RDS) is an easy-to-manage relational database service optimized for total cost of ownership.
    humanURL: https://aws.amazon.com/rds/
    baseURL: http://api.example.com
    tags:
      - Database
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ProgrammingGuide.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/aws-rds-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-aa69cacc-4bbf-4724-a1d4-78cdad57fee8?action=share&creator=35240
  - aid: apis-io-engineering-platform:aws-iam
    name: AWS IAM
    description: Amazon S3 is used for centralized object storage, managing all images, video, and audio across sites via public and private buckets.
    humanURL: https://aws.amazon.com/iam/
    baseURL: http://api.example.com
    tags:
      - Access
      - Identity
      - Keys
      - Tokens
      - Users
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/IAM/latest/APIReference/welcome.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/aws-iam-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-a5858f86-04d3-4e15-ae11-b42c7516688b?action=share&creator=35240
  - aid: apis-io-engineering-platform:microsoft-bing
    name: Microsoft Bing Search
    description: Amazon S3 is used for centralized object storage, managing all images, video, and audio across sites via public and private buckets.
    humanURL: https://www.microsoft.com/en-us/bing/apis
    baseURL: https://api.bing.microsoft.com
    tags:
      - Search
    properties:
      - type: Documentation
        url: https://www.microsoft.com/en-us/bing/apis/bing-web-search-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/microsoft-cognitive-web-search-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-c2052341-766c-43c7-b1dc-ed4985e4606b?action=share&creator=35240
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/microsoft-cognitive-video-search-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-aa777c90-8271-4809-8eac-3ec39a9a899c?action=share&creator=35240
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/microsoft-cognitive-news-search-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-aa777c90-8271-4809-8eac-3ec39a9a899c?action=share&creator=35240
  - aid: apis-io-engineering-platform:postman
    name: Postman
    description: Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs faster.
    humanURL: https://www.postman.com
    baseURL: http://api.example.com
    tags:
      - Storage
    properties:
      - type: Documentation
        url: https://example.com/documentation
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/postman-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-4d5957dc-df05-4216-a5fc-d46b3ba811d8?action=share&creator=35240
  - aid: apis-io-engineering-platform:cloudflare
    name: Cloudflare
    description: Cloudflare, Inc. is an American company that provides content delivery network services, cloud cybersecurity, DDoS mitigation, wide area network services, reverse proxies, Domain Name Service, and ICANN-accredited domain registration services.
    humanURL: https://developers.cloudflare.com/
    baseURL: https://api.cloudflare.com/
    tags:
      - DNS
    properties:
      - type: Documentation
        url: https://developers.cloudflare.com/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/cloudflare-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-28d97617-fdba-46a5-ac3e-40f3d2e0fa57?action=share&creator=35240
  - aid: apis-io-engineering-platform:github
    name: GitHub
    description: GitHub is a developer platform that allows developers to create, store, manage and share their code. It uses Git software, providing the distributed version control of Git plus access control, bug tracking, software feature requests, task management, continuous integration, and wikis for every project.
    humanURL: https://docs.github.com/en
    baseURL: https://api.github.com
    tags:
      - Pipelines
      - Source Control
    properties:
      - type: Documentation
        url: https://docs.github.com/en/rest
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-search/engineering-platform/refs/heads/main/openapi/github-openapi-original.yml
      - type: PostmanCollection
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-7429b451-d812-4abc-b497-b763372cf5c5?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-b0eafdd0-adaa-48a2-a855-6a31beb86d83?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-209f34ef-13c1-400c-bca8-fcddb304aff5?action=share&creator=35240
      - type: PostmanCapability
        url: https://api-evangelist.postman.co/workspace/APIs.io-Engineering-Platform/fe320942-e505-4ee8-8b7c-d72eae00d93f/collection/35240-fb2bbbb8-d4cc-48b1-a660-c8e158bfbbea?action=share&creator=35240
  - aid: apis-io-engineering-platform:vscode
    name: VSCode
    description: Visual Studio Code, also commonly referred to as VS Code, is an integrated development environment developed by Microsoft for Windows, Linux, macOS and web browsers.
    humanURL: https://code.visualstudio.com/
    tags:
      - IDE
    properties:
      - type: Documentation
        url: https://code.visualstudio.com/api/references/vscode-api
  - aid: apis-io-engineering-platform:aws-s3
    name: EasyCron
    description: EasyCron is used to run automated tasks, making API calls on a variety of schedules, using all of the APIs produced and consumed.
    humanURL: https://developer.easycron.com/
    baseURL: https://api.easycron.com
    tags:
      - CRON
      - Jobs
      - Scheduling
    properties:
      - type: Documentation
        url: https://developer.easycron.com/docs/api/v1/introduction
common:
  - type: PostmanPublicWorkspace
    url: https://www.postman.com/api-evangelist/workspace/apis-io/overview
  - type: GitHubOrganization
    url: https://github.com/api-search
  - type: Portals
    url: https://developer.apis.io/
maintainers:
  - FN: Kin Lane
    X-twitter: apievangelist
    email: kin@apievangelist.com
---
