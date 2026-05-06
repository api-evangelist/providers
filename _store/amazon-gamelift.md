---
aid: amazon-gamelift
name: Amazon GameLift
description: Amazon GameLift is a dedicated game server hosting solution that deploys, operates, and scales cloud servers for multiplayer games. It provides low-latency, low-cost server infrastructure, eliminates operational overhead, and allows you to focus on creating great gaming experiences. The service includes FlexMatch for matchmaking, FleetIQ for optimized Spot Instance usage, and Realtime Servers for rapid game server deployment.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Cloud Computing
  - Game Servers
  - Gaming
  - Multiplayer
  - Matchmaking
  - FlexMatch
  - FleetIQ
url: https://raw.githubusercontent.com/api-evangelist/amazon-gamelift/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-gamelift:amazon-gamelift-api
    name: Amazon GameLift API
    description: The Amazon GameLift API provides programmatic access to create and manage fleets, game sessions, player sessions, matchmaking configurations, and game server groups for hosting multiplayer game servers. It includes operations for managed hosting resources, FlexMatch matchmaking, FleetIQ optimization, and Realtime Servers configuration.
    humanURL: https://aws.amazon.com/gamelift/
    baseURL: https://gamelift.amazonaws.com
    tags:
      - Game Servers
      - Gaming
      - Multiplayer
      - Matchmaking
      - Fleets
      - Sessions
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/gamelift/latest/apireference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-gamelift-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/gamelift/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/gamelift/pricing/
      - type: FAQ
        url: https://aws.amazon.com/gamelift/faq/
      - type: APIReference
        url: https://docs.aws.amazon.com/gamelift/latest/apireference/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/gamelift/latest/apireference/CommonParameters.html
      - type: JSONSchema
        url: json-schema/gamelift-fleet-schema.json
      - type: JSONLD
        url: json-ld/amazon-gamelift-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/gamelift/
  - type: Documentation
    url: https://docs.aws.amazon.com/gamelift/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/gametech/tag/amazon-gamelift/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/gamelift/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SDK
    url: https://aws.amazon.com/developer/tools/
  - type: CLI
    url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html
  - type: Features
    data:
      - name: Managed Game Server Hosting
        description: Fully managed service to deploy, operate, and scale dedicated game servers with automatic lifecycle management for game and player sessions.
      - name: FlexMatch Matchmaking
        description: Customizable matchmaking service that connects up to 200 players into single game sessions based on configurable matching rules.
      - name: FleetIQ Optimization
        description: Optimizes use of low-cost Spot Instances for game hosting, improving viability and reducing costs while maintaining performance.
      - name: Realtime Servers
        description: Rapidly configurable game server framework with core Amazon GameLift infrastructure built in for quick deployment.
      - name: Auto Scaling
        description: Automatically scales fleet capacity up to 9,000 servers per minute to balance player demand and hosting costs.
      - name: Multi-Region Deployment
        description: Deploy game servers across multiple AWS regions with global queues for optimal player latency and resiliency.
      - name: Game Session Queues
        description: Multi-fleet, multi-region queues that use FleetIQ algorithms to prioritize game session placements based on latency, cost, and availability.
      - name: VPC Peering
        description: Create and manage VPC peering connections between GameLift hosting resources and other AWS resources.
      - name: Alias Management
        description: Create fleet aliases to simplify game server transitions and updates without changing client configurations.
  - type: UseCases
    data:
      - name: Multiplayer Game Launches
        description: Deploy and scale game servers for launch day without uncertainty about player demand using predictive autoscaling.
      - name: Session-Based Multiplayer
        description: Host dedicated game servers for real-time multiplayer games with low latency and high performance.
      - name: Player Matchmaking
        description: Use FlexMatch to create fair, customizable matchmaking for players based on skill level, region, and other criteria.
      - name: Cost-Optimized Hosting
        description: Leverage FleetIQ with Spot Instances to reduce game hosting costs while maintaining reliability.
      - name: Global Game Distribution
        description: Deploy game servers across multiple AWS regions to minimize player latency worldwide.
  - type: SpectralRules
    url: rules/amazon-gamelift-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-gamelift-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-gamelift-game-operations.yaml
  - type: Integrations
    data:
      - name: AWS EC2
        description: GameLift uses EC2 instances as the underlying compute for managed game server hosting.
      - name: AWS Auto Scaling
        description: Integrates with Auto Scaling groups for FleetIQ standalone deployment.
      - name: Amazon CloudWatch
        description: Monitor fleet metrics, game session activity, and performance data through CloudWatch.
      - name: Amazon SNS
        description: Receive notifications for matchmaking events and game session placement status.
      - name: AWS IAM
        description: Use IAM roles and policies to control access to GameLift resources and operations.
      - name: Amazon S3
        description: Store and retrieve game server build files using S3 buckets for fleet deployment.
      - name: AWS CloudFormation
        description: Provision and manage GameLift resources using infrastructure-as-code templates.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
