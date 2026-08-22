---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aws Waf Agentic Access
  operation_count: 1
  slug: aws-waf-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: 'REST API for creating and managing web ACLs, rule groups, IP sets, regex pattern sets, and logging configurations across regional and CloudFront-scoped AWS WAF deployments. Requests are authenticated '
  name: AWS WAFV2 API
  slug: wafv2-api
- description: The AWS WAFV2 API API from AWS WAF — 1 operation(s) for aws wafv2 api.
  name: AWS WAF AWS WAFV2 API API
  slug: aws-waf-aws-wafv2-api-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS WAFV2 AWS WAFV2 API API
  slug: open-aws-waf-aws-wafv2-api-api
- collection_type: open
  name: AWS WAFV2 API
  slug: open-aws-waf
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-waf-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-waf-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-waf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-waf-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-waf-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/waf/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/waf/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/waf/pricing/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/feed/
created: '2026-05-11'
description: AWS WAF is a web application firewall that monitors and controls HTTP and HTTPS requests forwarded to protected resources such as Amazon CloudFront distributions, API Gateway REST APIs, Application Load Balancers, AWS AppSync GraphQL APIs, Cognito user pools, App Runner services, Amplify applications, and Verified Access instances. It enables rule-based blocking, rate limiting, and managed rule groups to defend against common web exploits. The AWS WAFV2 API and AWS SDKs provide programmatic access using AWS Signature Version 4 authentication.
graphqls:
- description: ''
  name: AWS WAF GraphQL API
  slug: aws-waf-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-waf.png
layout: provider
modified: '2026-05-11'
name: AWS WAF
nav: Providers
network: true
overview: 'AWS WAF publishes 1 API on the [APIs.io](https://apis.io/) network: AWS WAFV2 API API. Tagged areas include Security, Web Application Firewall, DDoS Protection, Bot Management, and Edge Security.


  AWS WAF''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 32.6
  delta: -0.6
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 58.7
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-waf/refs/heads/main/screenshots/aws-waf-2026-06-20T172801.png
security:
- kind: authentication
  name: Aws Waf Authentication
  slug: aws-waf-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Waf Domain Security
  slug: aws-waf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Waf Vulnerability Disclosure
  slug: aws-waf-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Waf Trust Center
  slug: aws-waf-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-waf
tags:
- Security
- Web Application Firewall
- DDoS Protection
- Bot Management
- Edge Security
- Cloud
website: https://aws.amazon.com/waf/
---
