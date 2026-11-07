---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Armor Agentic Access
  operation_count: 7
  slug: google-cloud-armor-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: https://compute.googleapis.com/compute/v1
  baseurl_source: declared
  description: Manage individual rules within security policies
  name: Google Cloud Armor SecurityPolicyRules API
  slug: google-cloud-armor-securitypolicyrules-api
- baseURL: https://compute.googleapis.com/compute/v1
  baseurl_source: declared
  description: Manage security policies for Cloud Armor
  name: Google Cloud Armor Security Policies API
  slug: google-cloud-armor-security-policies-api
artifact_total: 16
collections:
- collection_type: postman
  name: Google Cloud Armor SecurityPolicies API
  slug: postman-google-cloud-armor-securitypolicies-api
- collection_type: postman
  name: Google Cloud Armor SecurityPolicies SecurityPolicyRules API
  slug: postman-google-cloud-armor-securitypolicyrules-api
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
- group: commercial
  href: https://artifacts.apis.io/google-cloud-armor/plans/google-cloud-armor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-armor-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-armor/rate-limits/google-cloud-armor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-armor-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-armor/finops/google-cloud-armor-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-armor-finops.yml
- group: other
  href: https://artifacts.apis.io/google-cloud-armor/capabilities/google-cloud-armor-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-armor-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-armor/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-armor/agentic-access/google-cloud-armor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-armor-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-armor/security/google-cloud-armor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-armor-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-armor/security/google-cloud-armor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-armor-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-armor/authentication/google-cloud-armor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-armor-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-armor/scopes/google-cloud-armor-scopes.yml
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
  href: https://artifacts.apis.io/google-cloud-armor/json-ld/json-ld.yml
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
- has_sources: true
  method: derived
  name: Google Cloud Armor Finops
  primary_unit: hour
  service_category: ''
  slug: google-cloud-armor-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-armor.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Armor
nav: Providers
network: true
overview: 'Google Cloud Armor publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: SecurityPolicyRules API and Security Policies API. Tagged areas include DDoS Protection, Firewall, Google Cloud, Security, and WAF.


  The Google Cloud Armor catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Armor''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Google Cloud Armor Plans Pricing
  plan_count: 9
  slug: google-cloud-armor-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Google Cloud Armor Rate Limits
  slug: google-cloud-armor-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Armor — jsonschema rules
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
  composite: 52.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.7
    catalog_earned_first_party: 12.0
    catalog_gap: 51.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 52.7
    developer_ergonomics: 51.2
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-cloud-armor/google-cloud-armor-2026-06-20T182043.png
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
website: https://www.google.com/
---
