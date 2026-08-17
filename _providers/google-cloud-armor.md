---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Armor Agentic Access
  operation_count: 7
  slug: google-cloud-armor-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 2
apis:
- description: Manage security policies for Cloud Armor
  name: Google Cloud Armor SecurityPolicies API
  slug: google-cloud-armor-securitypolicies-api
- description: Manage individual rules within security policies
  name: Google Cloud Armor SecurityPolicyRules API
  slug: google-cloud-armor-securitypolicyrules-api
artifact_total: 17
collections:
- collection_type: postman
  name: Google Cloud Armor SecurityPolicies API
  slug: postman-google-cloud-armor-securitypolicies-api
- collection_type: postman
  name: Google Cloud Armor SecurityPolicies SecurityPolicyRules API
  slug: postman-google-cloud-armor-securitypolicyrules-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Armor SecurityPolicies API
  slug: open-google-cloud-armor-securitypolicies-api
- collection_type: open
  name: Google Cloud Armor SecurityPolicies SecurityPolicyRules API
  slug: open-google-cloud-armor-securitypolicyrules-api
- collection_type: open
  name: Google Cloud Armor API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-armor/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-armor-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-armor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-armor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-armor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-armor-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/armor
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/armor/docs/configure-security-policies
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/armor/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/armor/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/armor/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/cloud-armor-release-notes.xml
created: '2026-03-13'
description: Google Cloud Armor provides DDoS protection and web application firewall (WAF) capabilities for Google Cloud applications, enabling you to create security policies that protect your services from attacks and unwanted traffic.
finops:
- name: Google Cloud Armor Finops
  service_category: API
  slug: google-cloud-armor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-armor.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Armor
nav: Providers
network: true
overview: 'Google Cloud Armor publishes 2 APIs on the [APIs.io](https://apis.io/) network: SecurityPolicies API and SecurityPolicyRules API. Tagged areas include DDoS Protection, Firewall, Google Cloud, Security, and WAF.


  The Google Cloud Armor catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Armor''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Cloud Armor Plans Pricing
  plan_count: 3
  slug: google-cloud-armor-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Google Cloud Armor Rate Limits
  slug: google-cloud-armor-rate-limits
rules:
- name: Google Cloud Armor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-armor-jsonschema-spectral-rules
scopes:
- name: Google Cloud Armor Scopes
  scope_count: 2
  slug: google-cloud-armor-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.2
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-armor/refs/heads/main/screenshots/google-cloud-armor-2026-06-20T182043.png
security:
- kind: authentication
  name: Google Cloud Armor Authentication
  slug: google-cloud-armor-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Armor Domain Security
  slug: google-cloud-armor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Armor Vulnerability Disclosure
  slug: google-cloud-armor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-armor
tags:
- DDoS Protection
- Firewall
- Google Cloud
- Security
- WAF
website: https://cloud.google.com/armor
---
