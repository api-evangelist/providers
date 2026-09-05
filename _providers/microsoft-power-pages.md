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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Power Pages Agentic Access
  operation_count: 6
  slug: microsoft-power-pages-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 3
apis:
- description: The Power Pages Web API provides CRUD operations on Dataverse tables from Power Pages websites. It enables authenticated and anonymous users to interact with business data through portal pages using s
  name: Power Pages Web API
  slug: web-api
- baseURL: https://{site}.powerappsportals.com/_api/
  baseurl_source: declared
  description: The Records API from Microsoft Power Pages — 2 operation(s) for records.
  name: Microsoft Power Pages Records API
  slug: microsoft-power-pages-records-api
- baseURL: https://{site}.powerappsportals.com/_api/
  baseurl_source: declared
  description: The Tables API from Microsoft Power Pages — 2 operation(s) for tables.
  name: Microsoft Power Pages Tables API
  slug: microsoft-power-pages-tables-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Power Pages Web Records API
  slug: open-microsoft-power-pages-records-api
- collection_type: open
  name: Microsoft Power Pages Web Records Tables API
  slug: open-microsoft-power-pages-tables-api
- collection_type: open
  name: Microsoft Power Pages Web API
  slug: open-microsoft-power-pages
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-power-pages-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-power-pages-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-power-pages-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-power-pages-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://make.powerpages.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://powerpages.microsoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-pages/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/power-pages/getting-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: Community
  url: https://community.powerplatform.com/forums/thread/?threadid=4f8c3d6b-df78-ef11-a317-7c1e522703d5
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/power-platform/blog/power-pages/feed/
created: '2024-01-01'
description: Microsoft Power Pages is a secure, enterprise-grade, low-code platform for creating, hosting, and administering modern external-facing business websites. It provides APIs for CRUD operations on Dataverse tables from portal pages.
finops:
- name: Microsoft Power Pages Finops
  service_category: API
  slug: microsoft-power-pages-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-power-pages.png
layout: provider
modified: '2026-04-28'
name: Microsoft Power Pages
nav: Providers
network: true
overview: 'Microsoft Power Pages publishes 2 APIs on the [APIs.io](https://apis.io/) network: Records API and Tables API. Tagged areas include Dataverse, Low-Code, Microsoft, and Web Portals.


  Microsoft Power Pages'' developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Power Pages Plans Pricing
  plan_count: 3
  slug: microsoft-power-pages-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Microsoft Power Pages Rate Limits
  slug: microsoft-power-pages-rate-limits
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-power-pages/refs/heads/main/screenshots/microsoft-power-pages-2026-06-20T185523.png
security:
- kind: authentication
  name: Microsoft Power Pages Authentication
  slug: microsoft-power-pages-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Power Pages Domain Security
  slug: microsoft-power-pages-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Power Pages Vulnerability Disclosure
  slug: microsoft-power-pages-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-power-pages
tags:
- Dataverse
- Low-Code
- Microsoft
- Web Portals
website: https://powerpages.microsoft.com/
---
