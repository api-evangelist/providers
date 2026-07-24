---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Chickfila Agentic Access
  operation_count: 27
  slug: chickfila-agentic-access
  summary_line: 27 operations · 1 acting
api_count: 15
apis:
- description: The Chick-fil-A mobile app provides mobile ordering, in-restaurant pickup, curbside, drive-thru express, and delivery ordering. The app manages Chick-fil-A One loyalty membership, points balance, tier
  name: Chick-fil-A Mobile App
  slug: chick-fil-a-mobile-app
- description: Chick-fil-A One is the tiered loyalty rewards program with four levels (Member, Silver, Red, Signature) offering 10-13 points per dollar, food rewards starting at 200 points, member-tier benefits incl
  name: Chick-fil-A One
  slug: chick-fil-a-one
- description: Chick-fil-A's online ordering platform at order.chick-fil-a.com supports pickup, drive-thru, curbside, dine-in, and delivery ordering. Integrated with the Chick-fil-A One loyalty program for points ea
  name: Chick-fil-A Online Ordering
  slug: chick-fil-a-ordering
- description: Chick-fil-A's catering platform for ordering party trays, packaged meals, entrees, and sides for groups. Supports same-day and advance scheduling, with pickup or delivery via local restaurant coordina
  name: Chick-fil-A Catering
  slug: chick-fil-a-catering
- description: Chick-fil-A eGift Cards in denominations from $5 to $100 are deliverable via email and redeemable in-restaurant, through the mobile app, and via the online ordering platform.
  name: Chick-fil-A eGift Cards
  slug: chick-fil-a-egift-cards
- description: Chick-fil-A restaurant locator for finding nearby locations with filters for services such as drive-thru, dine-in, delivery, catering, and curbside pickup, plus hours and contact info.
  name: Chick-fil-A Restaurant Locator
  slug: chick-fil-a-restaurant-locator
- description: AWS account inventory and metadata operations.
  name: Chick-fil-A Accounts API
  slug: chickfila-accounts-api
- description: Compliance rules and audit report operations.
  name: Chick-fil-A Compliance API
  slug: chickfila-compliance-api
- description: EC2 instances and public IP address operations.
  name: Chick-fil-A Compute API
  slug: chickfila-compute-api
- description: RDS, DynamoDB, and Redshift inventory.
  name: Chick-fil-A Databases API
  slug: chickfila-databases-api
- description: IAM users and roles across accounts.
  name: Chick-fil-A Identity API
  slug: chickfila-identity-api
- description: Security groups and load balancers.
  name: Chick-fil-A Networking API
  slug: chickfila-networking-api
- description: S3 bucket inventory and object listing.
  name: Chick-fil-A Storage API
  slug: chickfila-storage-api
- description: Aggregate counts across accounts.
  name: Chick-fil-A Summary API
  slug: chickfila-summary-api
- description: Health and configuration operations.
  name: Chick-fil-A System API
  slug: chickfila-system-api
artifact_total: 130
collections:
- collection_type: open
  name: Chick-fil-A BOVINE API
  slug: open-chickfila-bovine
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chickfila-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chickfila-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chick-fil-a
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chick-fil-a-corporate
- group: company
  title: ''
  type: Website
  url: https://www.chick-fil-a.com/
- group: start
  title: ''
  type: Login
  url: https://www.chick-fil-a.com/sign-in
- group: start
  title: ''
  type: Signup
  url: https://www.chick-fil-a.com/sign-up
- group: other
  title: ''
  type: Ordering
  url: https://order.chick-fil-a.com/
- group: design
  title: ''
  type: Rules
  url: rules/chickfila-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/chickfila-vocabulary.yml
- group: company
  title: Chick-fil-A Tech Blog
  type: Blog
  url: https://medium.com/chick-fil-atech
- group: build
  title: gha-docker-run GitHub Action
  type: Tools
  url: https://github.com/chick-fil-a/gha-docker-run
- group: build
  title: gha-clear-workspace GitHub Action
  type: Tools
  url: https://github.com/chick-fil-a/gha-clear-workspace
- group: build
  title: HoovesUp Bare-Metal SSM Bootstrap
  type: Tools
  url: https://github.com/chick-fil-a/hoovesup
- group: build
  title: GitOps Edge Kubernetes Demo
  type: CodeExamples
  url: https://github.com/chick-fil-a/gitops
- group: build
  title: Kustomize Application Feeder Repository
  type: CodeExamples
  url: https://github.com/chick-fil-a/kustomize-application
created: '2026-05-05'
description: Chick-fil-A is an American fast-food restaurant chain specializing in chicken sandwiches and operating over 3,000 locations across the United States. Known for customer service and a closed-on-Sunday policy, Chick-fil-A operates the Chick-fil-A One tiered loyalty program, the Chick-fil-A mobile app for ordering and rewards, the catering platform, and eGift Cards.
examples:
- key_count: 1
  name: Bovine Account Detail Example
  slug: bovine-account-detail-example
- key_count: 5
  name: Bovine Account List Item Example
  slug: bovine-account-list-item-example
- key_count: 5
  name: Bovine Add Account Request Example
  slug: bovine-add-account-request-example
- key_count: 1
  name: Bovine Add Account Response Example
  slug: bovine-add-account-response-example
- key_count: 2
  name: Bovine Compliance Rule Example
  slug: bovine-compliance-rule-example
- key_count: 2
  name: Bovine Count Summary Example
  slug: bovine-count-summary-example
- key_count: 1
  name: Bovine Dashboard Summary Example
  slug: bovine-dashboard-summary-example
- key_count: 2
  name: Bovine Dynamo Table Example
  slug: bovine-dynamo-table-example
- key_count: 1
  name: Bovine Dynamo Table List Example
  slug: bovine-dynamo-table-list-example
- key_count: 2
  name: Bovine Ec2 Instance Detail Example
  slug: bovine-ec2-instance-detail-example
- key_count: 3
  name: Bovine Ec2 Instance Example
  slug: bovine-ec2-instance-example
- key_count: 1
  name: Bovine Iam Role Example
  slug: bovine-iam-role-example
- key_count: 2
  name: Bovine Iam User Detail Example
  slug: bovine-iam-user-detail-example
- key_count: 2
  name: Bovine Iam User Summary Example
  slug: bovine-iam-user-summary-example
- key_count: 2
  name: Bovine Load Balancer Detail Example
  slug: bovine-load-balancer-detail-example
- key_count: 2
  name: Bovine Load Balancer Example
  slug: bovine-load-balancer-example
- key_count: 1
  name: Bovine Load Balancer List Example
  slug: bovine-load-balancer-list-example
- key_count: 1
  name: Bovine Message Response Example
  slug: bovine-message-response-example
- key_count: 1
  name: Bovine Ping Response Example
  slug: bovine-ping-response-example
- key_count: 4
  name: Bovine Public Ip Example
  slug: bovine-public-ip-example
- key_count: 5
  name: Bovine Rds Database Example
  slug: bovine-rds-database-example
- key_count: 3
  name: Bovine Redshift Cluster Example
  slug: bovine-redshift-cluster-example
- key_count: 1
  name: Bovine Redshift Cluster List Example
  slug: bovine-redshift-cluster-list-example
- key_count: 2
  name: Bovine Report Example
  slug: bovine-report-example
- key_count: 1
  name: Bovine Run Report Response Example
  slug: bovine-run-report-response-example
- key_count: 1
  name: Bovine S3 Bucket Detail Example
  slug: bovine-s3-bucket-detail-example
- key_count: 3
  name: Bovine S3 Bucket Example
  slug: bovine-s3-bucket-example
- key_count: 4
  name: Bovine Security Group Detail Example
  slug: bovine-security-group-detail-example
- key_count: 3
  name: Bovine Security Group Example
  slug: bovine-security-group-example
- key_count: 1
  name: Bovine Security Group List Example
  slug: bovine-security-group-list-example
- key_count: 4
  name: Bovine Security Group Rule Example
  slug: bovine-security-group-rule-example
features:
- description: Order ahead via the mobile app for pickup, drive-thru, curbside, dine-in, or delivery.
  name: Mobile Ordering
- description: Chick-fil-A One offers four-tier loyalty status with escalating point rates and benefits.
  name: Tiered Loyalty
- description: Earn 10 to 13 points per dollar; redeem from 200 points for food rewards.
  name: Point Earning and Redemption
- description: Silver and higher tier members can gift earned rewards to other members.
  name: Gifted Rewards
- description: Automatic birthday reward delivered through the mobile app.
  name: Birthday Rewards
- description: Group catering ordering with same-day and advance options.
  name: Catering Orders
- description: Email-deliverable digital gift cards in multiple denominations.
  name: eGift Cards
- description: Find nearby Chick-fil-A locations with services and hours.
  name: Restaurant Locator
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chickfila.png
integrations:
- description: Third-party delivery integration for home delivery of Chick-fil-A orders.
  name: DoorDash
- description: Third-party delivery integration via Uber Eats marketplace.
  name: Uber Eats
- description: Third-party delivery integration via Grubhub marketplace.
  name: Grubhub
json_schemas:
- name: AccountDetail
  property_count: 1
  slug: bovine-account-detail
- name: AccountListItem
  property_count: 5
  slug: bovine-account-list-item
- name: AddAccountRequest
  property_count: 5
  slug: bovine-add-account-request
- name: AddAccountResponse
  property_count: 1
  slug: bovine-add-account-response
- name: ComplianceRule
  property_count: 2
  slug: bovine-compliance-rule
- name: CountSummary
  property_count: 2
  slug: bovine-count-summary
- name: DashboardSummary
  property_count: 1
  slug: bovine-dashboard-summary
- name: DynamoTableList
  property_count: 1
  slug: bovine-dynamo-table-list
- name: DynamoTable
  property_count: 2
  slug: bovine-dynamo-table
- name: Ec2InstanceDetail
  property_count: 2
  slug: bovine-ec2-instance-detail
- name: Ec2Instance
  property_count: 3
  slug: bovine-ec2-instance
- name: IamRole
  property_count: 1
  slug: bovine-iam-role
- name: IamUserDetail
  property_count: 2
  slug: bovine-iam-user-detail
- name: IamUserSummary
  property_count: 2
  slug: bovine-iam-user-summary
- name: LoadBalancerDetail
  property_count: 2
  slug: bovine-load-balancer-detail
- name: LoadBalancerList
  property_count: 1
  slug: bovine-load-balancer-list
- name: LoadBalancer
  property_count: 2
  slug: bovine-load-balancer
- name: MessageResponse
  property_count: 1
  slug: bovine-message-response
- name: PingResponse
  property_count: 1
  slug: bovine-ping-response
- name: PublicIp
  property_count: 4
  slug: bovine-public-ip
- name: RdsDatabase
  property_count: 5
  slug: bovine-rds-database
- name: RedshiftClusterList
  property_count: 1
  slug: bovine-redshift-cluster-list
- name: RedshiftCluster
  property_count: 3
  slug: bovine-redshift-cluster
- name: Report
  property_count: 2
  slug: bovine-report
- name: RunReportResponse
  property_count: 1
  slug: bovine-run-report-response
- name: S3BucketDetail
  property_count: 1
  slug: bovine-s3-bucket-detail
- name: S3Bucket
  property_count: 3
  slug: bovine-s3-bucket
- name: SecurityGroupDetail
  property_count: 4
  slug: bovine-security-group-detail
- name: SecurityGroupList
  property_count: 1
  slug: bovine-security-group-list
- name: SecurityGroupRule
  property_count: 4
  slug: bovine-security-group-rule
- name: SecurityGroup
  property_count: 3
  slug: bovine-security-group
json_structures:
- name: Bovine Account Detail Structure
  property_count: 1
  slug: bovine-account-detail-structure
- name: Bovine Account List Item Structure
  property_count: 5
  slug: bovine-account-list-item-structure
- name: Bovine Add Account Request Structure
  property_count: 5
  slug: bovine-add-account-request-structure
- name: Bovine Add Account Response Structure
  property_count: 1
  slug: bovine-add-account-response-structure
- name: Bovine Compliance Rule Structure
  property_count: 2
  slug: bovine-compliance-rule-structure
- name: Bovine Count Summary Structure
  property_count: 2
  slug: bovine-count-summary-structure
- name: Bovine Dashboard Summary Structure
  property_count: 1
  slug: bovine-dashboard-summary-structure
- name: Bovine Dynamo Table List Structure
  property_count: 1
  slug: bovine-dynamo-table-list-structure
- name: Bovine Dynamo Table Structure
  property_count: 2
  slug: bovine-dynamo-table-structure
- name: Bovine Ec2 Instance Detail Structure
  property_count: 2
  slug: bovine-ec2-instance-detail-structure
- name: Bovine Ec2 Instance Structure
  property_count: 3
  slug: bovine-ec2-instance-structure
- name: Bovine Iam Role Structure
  property_count: 1
  slug: bovine-iam-role-structure
- name: Bovine Iam User Detail Structure
  property_count: 2
  slug: bovine-iam-user-detail-structure
- name: Bovine Iam User Summary Structure
  property_count: 2
  slug: bovine-iam-user-summary-structure
- name: Bovine Load Balancer Detail Structure
  property_count: 2
  slug: bovine-load-balancer-detail-structure
- name: Bovine Load Balancer List Structure
  property_count: 1
  slug: bovine-load-balancer-list-structure
- name: Bovine Load Balancer Structure
  property_count: 2
  slug: bovine-load-balancer-structure
- name: Bovine Message Response Structure
  property_count: 1
  slug: bovine-message-response-structure
- name: Bovine Ping Response Structure
  property_count: 1
  slug: bovine-ping-response-structure
- name: Bovine Public Ip Structure
  property_count: 4
  slug: bovine-public-ip-structure
- name: Bovine Rds Database Structure
  property_count: 5
  slug: bovine-rds-database-structure
- name: Bovine Redshift Cluster List Structure
  property_count: 1
  slug: bovine-redshift-cluster-list-structure
- name: Bovine Redshift Cluster Structure
  property_count: 3
  slug: bovine-redshift-cluster-structure
- name: Bovine Report Structure
  property_count: 2
  slug: bovine-report-structure
- name: Bovine Run Report Response Structure
  property_count: 1
  slug: bovine-run-report-response-structure
- name: Bovine S3 Bucket Detail Structure
  property_count: 1
  slug: bovine-s3-bucket-detail-structure
- name: Bovine S3 Bucket Structure
  property_count: 3
  slug: bovine-s3-bucket-structure
- name: Bovine Security Group Detail Structure
  property_count: 4
  slug: bovine-security-group-detail-structure
- name: Bovine Security Group List Structure
  property_count: 1
  slug: bovine-security-group-list-structure
- name: Bovine Security Group Rule Structure
  property_count: 4
  slug: bovine-security-group-rule-structure
- name: Bovine Security Group Structure
  property_count: 3
  slug: bovine-security-group-structure
jsonld:
- class_count: 34
  name: Chickfila Bovine Context
  property_count: 73
  slug: chickfila-bovine-context
layout: provider
modified: '2026-06-02'
name: Chick-fil-A
nav: Providers
network: true
overview: 'Chick-fil-A publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Compliance API, Compute API, and 6 more. Tagged areas include Fast Food, Restaurants, Food & Beverage, Loyalty, and Mobile Ordering.


  The Chick-fil-A catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Chick-fil-A''s developer surface includes signup flow, engineering blog, tooling, code examples, and 12 more developer resources.'
random_paper: 8
rules:
- name: Chick-fil-A API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: chickfila-jsonschema-spectral-rules
- name: Chick-fil-A API Rules
  rule_count: 37
  severity_counts:
    error: 5
    hint: 0
    info: 11
    warn: 21
  slug: chickfila-spectral-rules
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 63.1
    developer_ergonomics: 2.2
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 36.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chickfila/refs/heads/main/screenshots/chickfila-2026-06-20T174304.png
security:
- kind: domain-security
  name: Chickfila Domain Security
  slug: chickfila-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chickfila
tags:
- Fast Food
- Restaurants
- Food & Beverage
- Loyalty
- Mobile Ordering
- Catering
use_cases:
- description: Order ahead through the app for in-store, drive-thru, or curbside pickup.
  name: Mobile Pickup
- description: Earn and redeem points across visits with tier progression.
  name: Loyalty Engagement
- description: Office, school, and event catering through the catering platform.
  name: Group Catering
- description: Order family-sized meals and trays for at-home dining.
  name: Family Meal Ordering
- description: Home delivery via partnered delivery services.
  name: Delivery Orders
website: https://www.chick-fil-a.com/
---
