---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-11-06'
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
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Byte Match Set API from AWS WAF — 5 operation(s) for waf byte match set.
  name: AWS WAF Waf Byte Match Set API
  slug: aws-waf-byte-match-set-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Geo Match Set API from AWS WAF — 5 operation(s) for waf geo match set.
  name: AWS WAF Waf Geo Match Set API
  slug: aws-waf-geo-match-set-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Logging Configuration API from AWS WAF — 4 operation(s) for waf logging configuration.
  name: AWS WAF Waf Logging Configuration API
  slug: aws-waf-logging-configuration-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Permission Policy API from AWS WAF — 3 operation(s) for waf permission policy.
  name: AWS WAF Waf Permission Policy API
  slug: aws-waf-permission-policy-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Rate Based Rule API from AWS WAF — 5 operation(s) for waf rate based rule.
  name: AWS WAF Waf Rate Based Rule API
  slug: aws-waf-rate-based-rule-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Regex Match Set API from AWS WAF — 5 operation(s) for waf regex match set.
  name: AWS WAF Waf Regex Match Set API
  slug: aws-waf-regex-match-set-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Regex Pattern Set API from AWS WAF — 5 operation(s) for waf regex pattern set.
  name: AWS WAF Waf Regex Pattern Set API
  slug: aws-waf-regex-pattern-set-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Rule API from AWS WAF — 5 operation(s) for waf rule.
  name: AWS WAF Waf Rule API
  slug: aws-waf-rule-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Size Constraint Set API from AWS WAF — 5 operation(s) for waf size constraint set.
  name: AWS WAF Waf Size Constraint Set API
  slug: aws-waf-size-constraint-set-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Sql Injection Match Set API from AWS WAF — 5 operation(s) for waf sql injection match set.
  name: AWS WAF Waf Sql Injection Match Set API
  slug: aws-waf-sql-injection-match-set-api
- baseURL: https://wafv2.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Waf Xss Match Set API from AWS WAF — 5 operation(s) for waf xss match set.
  name: AWS WAF Waf Xss Match Set API
  slug: aws-waf-xss-match-set-api
artifact_total: 29
collections:
- collection_type: open
  name: AWS WAFV2 AWS WAFV2 API API
  slug: open-aws-waf-aws-wafv2-api-api
- collection_type: open
  name: AWS WAFV2 API
  slug: open-aws-waf
common:
- group: commercial
  href: https://artifacts.apis.io/aws-waf/plans/aws-waf-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aws-waf-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/aws-waf/capabilities/aws-waf-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aws-waf-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/aws-waf/agentic-access/aws-waf-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-waf-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/aws-waf/security/aws-waf-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aws-waf-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aws-waf/security/aws-waf-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-waf-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aws-waf/security/aws-waf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aws-waf-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/aws-waf/authentication/aws-waf-authentication.yml
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
finops:
- has_sources: true
  method: derived
  name: Aws Waf Finops
  primary_unit: webacl
  service_category: ''
  slug: aws-waf-finops
  template: false
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
overview: 'AWS WAF publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including AWS WAFV2 API, IP Sets API, Rule Groups API, and 13 more. Tagged areas include Security, Web Application Firewall, DDoS Protection, Bot Management, and Edge Security.


  The AWS WAF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AWS WAF''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Aws Waf Plans Pricing
  plan_count: 6
  slug: aws-waf-plans-pricing
- name: Aws Waf Price Estimates
  plan_count: 0
  slug: aws-waf-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: AWS WAF API Rules
  rule_count: 64
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 2
  slug: aws-waf-rules
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 72.9
    catalog_earned_first_party: 12.0
    catalog_gap: 42.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 71.1
    contract_governance: 13.6
    contract_quality: 70.2
    developer_ergonomics: 50.0
    discoverability: 71.4
    operational_transparency: 26.3
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 73.3
      total: 15
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aws-waf/aws-waf-2026-06-20T172801.png
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
- Amazon Web Services
website: https://aws.amazon.com/waf/
---
