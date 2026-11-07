---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Orca Security's REST API provides programmatic access to the Orca Cloud Security Platform for querying cloud inventory and assets, managing alerts and risk findings, configuring integrations and autom
  name: Orca Security REST API
  slug: orca-security-rest-api
- description: SCIM 2.0 endpoint for provisioning and de-provisioning users and groups in Orca Security from identity providers such as Okta, Azure AD, and OneLogin.
  name: Orca Security SCIM 2.0 API
  slug: orca-security-scim-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/orca-security/plans/orca-security-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orca-security-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/orca-security/rate-limits/orca-security-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/orca-security-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/orca-security/finops/orca-security-finops.yml
  title: ''
  type: FinOps
  url: finops/orca-security-finops.yml
- group: auth
  href: https://artifacts.apis.io/orca-security/security/orca-security-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/orca-security-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/orca-security/security/orca-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orca-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orca.security/
- group: other
  title: ''
  type: Platform
  url: https://orca.security/platform/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orcasecurity.io/
- group: start
  title: ''
  type: Login
  url: https://app.orcasecurity.io/
- group: other
  title: ''
  type: RegionSelection
  url: https://region-selection.orcasecurity.io/
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/orcasecurity/orcasecurity/latest
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.orca.security/
- group: company
  title: ''
  type: Blog
  url: https://orca.security/resources/blog/
- group: other
  title: ''
  type: Resources
  url: https://orca.security/resources/
- group: other
  title: ''
  type: Customers
  url: https://orca.security/customers/
- group: company
  title: ''
  type: Partners
  url: https://orca.security/partners/
- group: company
  title: ''
  type: Careers
  url: https://orca.security/company/careers/
- group: company
  title: ''
  type: AboutUs
  url: https://orca.security/company/
- group: operate
  title: ''
  type: ContactSales
  url: https://orca.security/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orca-security/
created: '2026-05-23'
description: Orca Security is an agentless cloud security platform that uses its patented SideScanning technology to provide visibility into risks across AWS, Azure, Google Cloud, Oracle Cloud, Kubernetes, and serverless environments, covering CSPM, CWPP, CIEM, DSPM, vulnerability management, malware detection, API security, and AI security in a single platform. Orca exposes a region-aware REST API for assets, alerts, integrations, automations, and user management, plus SCIM 2.0 for identity provisioning and a Terraform provider for infrastructure-as-code workflows.
finops:
- has_sources: false
  method: generated
  name: Orca Security Finops
  primary_unit: ''
  service_category: API
  slug: orca-security-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orca-security.png
layout: provider
modified: '2026-05-23'
name: Orca Security
nav: Providers
network: true
overview: 'Orca Security is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agentless, API Security, CIEM, Cloud Security, and CNAPP.


  Orca Security''s developer surface includes documentation, engineering blog, and 18 more developer resources.'
plans:
- name: Orca Security Plans Pricing
  plan_count: 1
  slug: orca-security-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Orca Security Rate Limits
  slug: orca-security-rate-limits
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 15.8
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/orca-security/orca-security-2026-06-20T191207.png
security:
- kind: domain-security
  name: Orca Security Domain Security
  slug: orca-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orca Security Vulnerability Disclosure
  slug: orca-security-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: orca-security
tags:
- Agentless
- API Security
- CIEM
- Cloud Security
- CNAPP
- CSPM
- CWPP
- DSPM
- SideScanning
- Vulnerability Management
website: https://orca.security/
---
