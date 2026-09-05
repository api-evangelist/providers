---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Waf Agentic Access
  operation_count: 5
  slug: amazon-waf-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 1
apis:
- baseURL: https://wafv2.amazonaws.com
  baseurl_source: declared
  description: The IP Sets API from Amazon WAF — 1 operation(s) for ip sets.
  name: Amazon WAF IP Sets API
  slug: amazon-waf-ip-sets-api
- baseURL: https://wafv2.amazonaws.com
  baseurl_source: declared
  description: The Rule Groups API from Amazon WAF — 1 operation(s) for rule groups.
  name: Amazon WAF Rule Groups API
  slug: amazon-waf-rule-groups-api
- baseURL: https://wafv2.amazonaws.com
  baseurl_source: declared
  description: The Web ACLs API from Amazon WAF — 3 operation(s) for web acls.
  name: Amazon WAF Web ACLs API
  slug: amazon-waf-web-acls-api
artifact_total: 36
collections:
- collection_type: postman
  name: Amazon WAF IP Sets API
  slug: postman-amazon-waf-ip-sets-api
- collection_type: postman
  name: Amazon WAF IP Sets Rule Groups API
  slug: postman-amazon-waf-rule-groups-api
- collection_type: postman
  name: Amazon WAF IP Sets Web ACLs API
  slug: postman-amazon-waf-web-acls-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon WAF IP Sets API
  slug: open-amazon-waf-ip-sets-api
- collection_type: open
  name: Amazon WAF IP Sets Rule Groups API
  slug: open-amazon-waf-rule-groups-api
- collection_type: open
  name: Amazon WAF IP Sets Web ACLs API
  slug: open-amazon-waf-web-acls-api
- collection_type: open
  name: Amazon WAF API
  slug: open-amazon-waf
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-waf/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-waf-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-waf-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-waf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-waf-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-waf-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
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
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/wafv2/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-waf
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-waf/refs/heads/main/rules/amazon-waf-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-waf/refs/heads/main/vocabulary/amazon-waf-vocabulary.yaml
created: '2024-01-15'
description: AWS WAF is a web application firewall that helps protect web applications and APIs from common web exploits and bots that may affect availability, compromise security, or consume excessive resources.
examples:
- key_count: 2
  name: Amazon Waf Example
  slug: amazon-waf-example
features:
- description: Automate operational tasks with Amazon WAF.
  name: Automation
- description: Programmatic access to Amazon WAF resources.
  name: API Access
finops:
- name: Amazon Waf Finops
  service_category: API
  slug: amazon-waf-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Rule
  property_count: 4
  slug: amazon-waf-rule
- name: Tag
  property_count: 2
  slug: amazon-waf-tag
- name: VisibilityConfig
  property_count: 3
  slug: amazon-waf-visibility-config
- name: WebACLSummary
  property_count: 4
  slug: amazon-waf-web-a-c-l-summary
- name: AWS WAF Web ACL
  property_count: 10
  slug: amazon-waf-web-acl
json_structures:
- name: Amazon Waf Rule Structure
  property_count: 0
  slug: amazon-waf-rule-structure
- name: Amazon Waf Tag Structure
  property_count: 0
  slug: amazon-waf-tag-structure
- name: Amazon Waf Visibility Config Structure
  property_count: 0
  slug: amazon-waf-visibility-config-structure
- name: Amazon Waf Web A C L Summary Structure
  property_count: 0
  slug: amazon-waf-web-a-c-l-summary-structure
- name: Amazon Waf Web Acl Structure
  property_count: 0
  slug: amazon-waf-web-acl-structure
jsonld:
- class_count: 7
  name: Amazon Waf Context
  property_count: 5
  slug: amazon-waf-context
layout: provider
modified: '2026-05-19'
name: Amazon WAF
nav: Providers
network: true
overview: 'Amazon WAF publishes 3 APIs on the [APIs.io](https://apis.io/) network: IP Sets API, Rule Groups API, and Web ACLs API. Tagged areas include Bot Management, DDoS Protection, Security, WAF, and Web Application Firewall.


  The Amazon WAF catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon WAF''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 17 more developer resources.'
plans:
- name: Amazon Waf Plans Pricing
  plan_count: 3
  slug: amazon-waf-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Amazon Waf Rate Limits
  slug: amazon-waf-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon WAF API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-waf-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Amazon WAF API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 10
  slug: amazon-waf-spectral-rules
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 72.6
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 58.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-waf/refs/heads/main/screenshots/amazon-waf-2026-06-20T171845.png
security:
- kind: authentication
  name: Amazon Waf Authentication
  slug: amazon-waf-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Waf Domain Security
  slug: amazon-waf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Waf Vulnerability Disclosure
  slug: amazon-waf-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Waf Trust Center
  slug: amazon-waf-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-waf
tags:
- Bot Management
- DDoS Protection
- Security
- WAF
- Web Application Firewall
use_cases:
- description: Use Amazon WAF to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/waf/
---
