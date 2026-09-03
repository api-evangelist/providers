---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://envisagenow.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.acadis.com/ — a different registrable domain (envisagenow.com -> acadis.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://envisagenow.com
- group: company
  title: ''
  type: Blog
  url: https://www.acadis.com/types/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.acadis.com/contact-acadis/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acadis.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://community.envisagenow.com/cares/s/login/
- group: start
  title: ''
  type: Portal
  url: https://community.envisagenow.com/cares/s/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/envisagenow-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/envisagenow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/envisagenow-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/envisagenow-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envisagenow-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/envisagenow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.acadis.com/acadis-security-issue-reporting/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/envisagenow-llms.txt
created: '2026-07-17'
description: Envisage Technologies LLC builds the Acadis Readiness Suite, a unified public-safety training, compliance, and performance management software platform used by more than 10,000 agencies and 2 million-plus first responders across law enforcement, fire and rescue, corrections, emergency communications, federal, military, and local-government organizations. Product lines include the Acadis Readiness Suite (recruit & hire, training & testing, compliance management, academy automation, performance management, internal affairs and case management, inventory, budgeting, and a blended/virtual LMS), Guardian Tracking (an early-intervention system for smaller agencies), and the Acadis Network for individuals. The company operates as envisagenow.com (now redirecting to acadis.com) and is a portfolio company of Norwest Venture Partners. Envisage publishes no public developer API; this profile is API Evangelist enrichment assembled from publicly discoverable surfaces only, including the
  Acadis Readiness Community Salesforce Experience Cloud identity provider.
image: https://www.acadis.com/wp-content/uploads/2021/08/home-banner-img.jpg
layout: provider
modified: '2026-07-19'
name: Envisagenow
nav: Providers
network: true
overview: 'Envisagenow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Public Safety, Training, Compliance, and Performance Management.


  Envisagenow''s developer surface includes engineering blog, support, developer portal, authentication, and 10 more developer resources.'
random_paper: 14
scopes:
- name: Envisagenow Scopes
  scope_count: 36
  slug: envisagenow-scopes
  summary_line: 36 scopes · authorizationCode
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 25.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 68.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/envisagenow/refs/heads/main/screenshots/envisagenow-2026-07-25T213448.png
security:
- kind: authentication
  name: Envisagenow Authentication
  slug: envisagenow-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Envisagenow Domain Security
  slug: envisagenow-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Envisagenow Vulnerability Disclosure
  slug: envisagenow-vulnerability-disclosure
  summary_line: Hackerone
slug: envisagenow
tags:
- Company
- Public Safety
- Training
- Compliance
- Performance Management
- Law Enforcement
- First Responders
- Government
- Software-as-a-Service
website: https://envisagenow.com
---
