---
access_model:
  confidence: high
  label: Vendor-issued API key
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - https://developer.brandcast.io/
  - plans/brandcast-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Brandcast Agentic Access
  operation_count: 26
  slug: brandcast-agentic-access
  summary_line: 26 operations · 12 acting · 1 human-in-the-loop
api_count: 9
apis:
- baseURL: https://api.brandcast-prod.io
  baseurl_source: declared
  description: The Account API from Brandcast — 1 operation(s) for account.
  name: Brandcast Account API
  slug: brandcast-account-api
- baseURL: https://api.brandcast-prod.io
  baseurl_source: declared
  description: The Salesforce API from Brandcast — 1 operation(s) for salesforce.
  name: Brandcast Salesforce API
  slug: brandcast-salesforce-api
- baseURL: https://api.brandcast-prod.io
  baseurl_source: declared
  description: The Templates API from Brandcast — 4 operation(s) for templates.
  name: Brandcast Templates API
  slug: brandcast-templates-api
- baseURL: https://api.brandcast-prod.io
  baseurl_source: declared
  description: The Websites API from Brandcast — 13 operation(s) for websites.
  name: Brandcast Websites API
  slug: brandcast-websites-api
artifact_total: 15
collections:
- collection_type: open
  name: Brandcast Account API
  slug: open-brandcast-account
- collection_type: open
  name: Brandcast Salesforce API
  slug: open-brandcast-salesforce
- collection_type: open
  name: Brandcast Templates API
  slug: open-brandcast-templates
- collection_type: open
  name: Brandcast Websites API
  slug: open-brandcast-websites
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/brandcast-websites-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brandcast-templates-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brandcast-salesforce-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brandcast-account-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brandcast-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.brandcast.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.brandcast.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/brandcast-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brandcast-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brandcast-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brandcast
- group: company
  title: ''
  type: Website
  url: https://www.brandcast.com
- group: start
  title: ''
  type: GettingStarted
  url: https://tutorials.sites.design/
- group: operate
  title: ''
  type: Support
  url: https://support.timesites.com/en/
- group: start
  title: ''
  type: Login
  url: https://app.brandcast.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sites.design/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sites.design/privacy-policy/
- group: design
  title: ''
  type: Conventions
  url: conventions/brandcast-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brandcast-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brandcast-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brandcast-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brandcast-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brandcast-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brandcast-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/brandcast-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/brandcast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brandcast-rate-limits.yml
created: '2026-07-17'
description: Brandcast is a no-code digital customer experience and website platform, founded in 2013 and backed by Shasta Ventures, that fuses web design, content creation, and brand asset management into a single system. Business and marketing teams use its Design Studio to build and maintain branded websites, sales proposals, brochures, and content programs, with Salesforce integration for personalized, trackable sites. The Brandcast API opens the Design Studio to developers to create websites from templates and update site content, authenticated with an API key sent in the x-api-key header over HTTPS. Brandcast's website product has since been rebranded as "Sites" and joined Vev; the developer API portal remains at developer.brandcast.io.
image: https://brandcast-cdn.global.ssl.fastly.net/61c3bb24-acd1-4c34-a5e0-3af04a2afb9a/71efcf85-6914-4a7e-9e50-1667c8d865f7/3c7a4af9ee3e6c75f4a0153bd866a9d9/brandcast.png
layout: provider
modified: '2026-08-13'
name: Brandcast
nav: Providers
network: true
overview: 'Brandcast publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Salesforce API, Templates API, and 1 more. Tagged areas include Company, Enterprise Software, No-Code, Website Builder, and Content Management.


  Brandcast''s developer surface includes documentation, authentication, getting-started guide, support, changelog, and 23 more developer resources.'
plans:
- name: Brandcast Plans Pricing
  plan_count: 0
  slug: brandcast-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Brandcast Rate Limits
  slug: brandcast-rate-limits
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 60.5
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brandcast/refs/heads/main/screenshots/brandcast-2026-07-25T203717.png
security:
- kind: authentication
  name: Brandcast Authentication
  slug: brandcast-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Brandcast Domain Security
  slug: brandcast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brandcast Vulnerability Disclosure
  slug: brandcast-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Brandcast Trust Center
  slug: brandcast-trust-center
  summary_line: count, named, note
slug: brandcast
tags:
- Company
- Enterprise Software
- No-Code
- Website Builder
- Content Management
- Digital Experience
- Web Design
- Brand Management
website: https://www.brandcast.com
---
