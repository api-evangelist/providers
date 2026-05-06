---
name: Amazon Elastic Load Balancing
description: Amazon Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions, ensuring high availability and fault tolerance for your applications.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/elasticloadbalancing/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Amazon Web Services
  - AWS
  - High Availability
  - Load Balancing
  - Networking
  - Scalability
apis:
  - name: Elastic Load Balancing v2 API
    description: API for managing Application Load Balancers (ALB), Network Load Balancers (NLB), and Gateway Load Balancers (GLB) with advanced routing and target group management.
    humanURL: https://aws.amazon.com/elasticloadbalancing/
    baseURL: https://elasticloadbalancing.amazonaws.com
    tags:
      - ALB
      - GLB
      - Load Balancing
      - Networking
      - NLB
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/
      - type: OpenAPI
        url: openapi/amazon-elastic-load-balancing-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/
      - type: GettingStarted
        url: https://aws.amazon.com/elasticloadbalancing/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/elasticloadbalancing/pricing/
      - type: FAQ
        url: https://aws.amazon.com/elasticloadbalancing/faqs/
      - type: JSONSchema
        url: json-schema/amazon-elastic-load-balancing-action-schema.json
      - type: JSONSchema
        url: json-schema/amazon-elastic-load-balancing-create-listener-response-schema.json
      - type: JSONSchema
        url: json-schema/amazon-elastic-load-balancing-create-load-balancer-response-schema.json
      - type: JSONLD
        url: json-ld/amazon-elastic-load-balancing-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/elasticloadbalancing/
  - type: Documentation
    url: https://docs.aws.amazon.com/elasticloadbalancing/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/ec2/home#LoadBalancers/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: FAQ
    url: https://aws.amazon.com/elasticloadbalancing/faqs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/elasticloadbalancing
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-elastic-load-balancing-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-elastic-load-balancing-capability.yaml
  - type: NaftikoCapability
    url: capabilities/shared/api.yaml
  - type: Vocabulary
    url: vocabulary/amazon-elastic-load-balancing-vocabulary.yaml
  - type: Features
    data:
      - name: Application Load Balancer
        description: HTTP/HTTPS load balancing with advanced request routing based on content
      - name: Network Load Balancer
        description: Ultra-high performance TCP/UDP load balancing at OSI layer 4
      - name: Gateway Load Balancer
        description: Distribute traffic to third-party virtual appliances for inspection
      - name: Health Checks
        description: Automatically route traffic away from unhealthy targets
      - name: SSL/TLS Termination
        description: Offload SSL/TLS decryption from application servers
  - type: UseCases
    data:
      - name: Web Application Load Balancing
        description: Distribute HTTP/HTTPS traffic across multiple web servers
      - name: Microservices Routing
        description: Route requests to different microservices based on URL paths or headers
      - name: Container Load Balancing
        description: Load balance traffic to ECS containers and Kubernetes pods
      - name: Multi-Region Traffic Management
        description: Distribute global traffic across multiple AWS regions
  - type: Integrations
    data:
      - name: Amazon EC2
        description: Distribute traffic across EC2 instances
      - name: Amazon ECS
        description: Load balance traffic to containerized applications
      - name: AWS Lambda
        description: Route HTTP requests directly to Lambda functions
      - name: Amazon Route 53
        description: Integrate with DNS for global traffic routing
      - name: AWS WAF
        description: Protect applications from web exploits and bots
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
