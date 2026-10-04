---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Aws Waf Agentic Access
  operation_count: 6
  slug: aws-waf-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 4
apis:
- description: 'REST API for creating and managing web ACLs, rule groups, IP sets, regex pattern sets, and logging configurations across regional and CloudFront-scoped AWS WAF deployments. Requests are authenticated '
  name: AWS WAFV2 API
  slug: wafv2-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The AWS WAFV2 API API from AWS WAF — 1 operation(s) for aws wafv2 api.
  name: AWS WAF AWS WAFV2 API
  slug: aws-waf-aws-wafv2-api-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The IP Sets API from AWS WAF — 1 operation(s) for ip sets.
  name: AWS WAF IP Sets API
  slug: aws-waf-ip-sets-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Rule Groups API from AWS WAF — 1 operation(s) for rule groups.
  name: AWS WAF Rule Groups API
  slug: aws-waf-rule-groups-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Web ACLs API from AWS WAF — 3 operation(s) for web acls.
  name: AWS WAF Web ACLs API
  slug: aws-waf-web-acls-api
artifact_total: 15
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
  href: https://raw.githubusercontent.com/api-evangelist/aws-waf/refs/heads/main/agentic-access/aws-waf-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-waf-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aws-waf/refs/heads/main/security/aws-waf-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aws-waf-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aws-waf/refs/heads/main/security/aws-waf-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-waf-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aws-waf/refs/heads/main/security/aws-waf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aws-waf-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aws-waf/refs/heads/main/authentication/aws-waf-authentication.yml
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-waf.png
json_schemas:
- name: AWS WAF Web ACL
  property_count: 10
  slug: amazon-waf-web-acl
jsonld:
- class_count: 7
  name: Amazon Waf Context
  property_count: 5
  slug: amazon-waf-context
layout: provider
modified: '2026-09-16'
name: AWS WAF
nav: Providers
network: true
overview: 'AWS WAF publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AWS WAFV2 API, IP Sets API, Rule Groups API, and 2 more. Tagged areas include Security, Web Application Firewall, DDoS Protection, Bot Management, and Edge Security.


  The AWS WAF catalog on APIs.io includes 1 JSON-LD context.


  AWS WAF''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 53.4
    catalog_earned_first_party: 0.0
    catalog_gap: 61.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 61.8
    developer_ergonomics: 50.0
    discoverability: 71.4
    operational_transparency: 26.3
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
