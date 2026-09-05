---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ripe Insurance Agentic Access
  operation_count: 8
  slug: ripe-insurance-agentic-access
  summary_line: 8 operations
api_count: 2
apis:
- baseURL: https://www.ripeinsurance.co.uk/umbraco/delivery/api/v2
  baseurl_source: declared
  description: The Content API from Ripe Insurance — 8 operation(s) for content.
  name: Ripe Insurance Content API
  slug: ripe-insurance-content-api
- baseURL: https://www.ripeinsurance.co.uk/umbraco/delivery/api/v2
  baseurl_source: declared
  description: The Media API from Ripe Insurance — 8 operation(s) for media.
  name: Ripe Insurance Media API
  slug: ripe-insurance-media-api
artifact_total: 8
collections:
- collection_type: open
  name: Umbraco Delivery API
  slug: open-ripe-insurance-cycleplan-content-delivery
- collection_type: open
  name: Umbraco Delivery API
  slug: open-ripe-insurance-umbraco-content-delivery
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ripe-insurance-umbraco-content-delivery-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ripe-insurance-cycleplan-content-delivery-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ripe-insurance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ripe-insurance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ripe-insurance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ripe-insurance-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ripe-insurance-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ripe-insurance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ripe-insurance-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ripe-insurance-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ripe-insurance-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ripe-insurance-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/ripe-insurance-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ripe-insurance-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ripe-insurance-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ripe-insurance-tool-crosswalk.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/ripe-insurance-openid-configuration.json
- group: company
  title: ''
  type: Website
  url: https://www.ripeinsurance.co.uk/
- group: company
  title: ''
  type: CorporateWebsite
  url: https://www.ripethinking.co.uk/
- group: company
  title: ''
  type: Partners
  url: https://www.ripethinking.co.uk/partner-with-us/
- group: other
  title: ''
  type: Technology
  url: https://www.ripethinking.co.uk/technology/
- group: company
  title: ''
  type: About
  url: https://www.ripeinsurance.co.uk/about/
- group: operate
  title: ''
  type: Support
  url: https://www.ripeinsurance.co.uk/help-and-support/
- group: other
  title: ''
  type: Claims
  url: https://www.ripeinsurance.co.uk/how-to-claim/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ripeinsurance.co.uk/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ripeinsurance.co.uk/privacy-policy/
- group: company
  title: ''
  type: News
  url: https://www.ripethinking.co.uk/news/
- group: company
  title: ''
  type: Blog
  url: https://www.ripeinsurance.co.uk/motorhome-insurance/blog/
- group: start
  title: ''
  type: Login
  url: https://www.ripeinsurance.co.uk/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RipeThinking
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/ripe-insurance
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: https://www.ripeinsurance.co.uk/.well-known/openid-configuration
created: '2026-07-25'
description: Ripe Insurance Services Limited, trading as Ripe and part of Ripe Thinking Limited, is a Stockport-based United Kingdom digital Managing General Agent and specialist insurance intermediary authorised and regulated by the Financial Conduct Authority (FRN 313411). Founded in 1997 and majority-backed by Aquiline Capital Partners, Ripe underwrites and distributes niche personal and small-commercial lines direct to consumers through its own brands — Cycleplan, Golf Care, Insure4Boats, Insure4Sport and Ripe Caravans — covering caravans and motorhomes, park homes and holiday homes, photography and music equipment, valuables, shooting, golf, cycling, boats, over 400 sports, personal trainers, hair and beauty businesses, clubs and leisure organisations, and small business. It reports more than 400,000 policyholders. Ripe's API posture is honestly assessed as partner-gated with no public developer surface — there is no developer portal, no self-serve API programme, no published quote,
  bind, issue or FNOL API, and no ACORD reference anywhere on its estate. Its in-house platform is marketed as flexible and fast to integrate, but partnering is a business-development contact form on ripethinking.co.uk rather than a technical onboarding path. The only anonymously reachable, machine-readable API surface across the Ripe brand estate is the Umbraco CMS Content Delivery API that ships with its .NET content management system — read-only content and media, incidental infrastructure rather than an insurance product API. Its April 2026 Cycleplan ChatGPT app delivers real-time cycling quotes conversationally, but is a first-party consumer channel with no published API, MCP server, or spec.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Ripe Insurance
nav: Providers
network: true
overview: 'Ripe Insurance publishes 2 APIs on the [APIs.io](https://apis.io/) network: Content API and Media API. Tagged areas include Insurance, United Kingdom, Insurtech, Managing General Agent, and Specialist Insurance.


  Ripe Insurance''s developer surface includes authentication, support, product news, engineering blog, and 29 more developer resources.'
random_paper: 17
scopes:
- name: Ripe Insurance Scopes
  scope_count: 2
  slug: ripe-insurance-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 39.5
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ripe-insurance/refs/heads/main/screenshots/ripe-insurance-2026-09-02T153839.png
security:
- kind: authentication
  name: Ripe Insurance Authentication
  slug: ripe-insurance-authentication
  summary_line: none/apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Ripe Insurance Domain Security
  slug: ripe-insurance-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ripe-insurance
tags:
- Insurance
- United Kingdom
- Insurtech
- Managing General Agent
- Specialist Insurance
- Personal Lines
- Small Business Insurance
- Underwriting
- Direct to Consumer
- Brokers
website: https://www.ripeinsurance.co.uk/
---
