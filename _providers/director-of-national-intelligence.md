---
access_model:
  confidence: medium
  label: Free and open — anonymous, unauthenticated public read API; no signup, no key, no plans
  onboarding: unknown
  pricing: free
  public: true
  source:
  - '{''url'': ''https://www.odni.gov/?rest_route=/wp/v2/posts&per_page=3'', ''status'': 200, ''note'': ''returns JSON anonymously with no credential of any kind (probed 2026-09-06)''}'
  - '{''url'': ''https://www.dni.gov/'', ''status'': 301, ''note'': ''the previously declared website redirects to https://www.odni.gov/ — a different registrable domain (dni.gov -> odni.gov); Website pointer moved to odni.gov on 2026-09-06''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-06'
api_count: 1
apis:
- baseURL: https://www.odni.gov/?rest_route=/
  baseurl_source: declared
  description: The anonymous, read-only WordPress REST API behind www.odni.gov. Serves ODNI newsroom posts (press releases, remarks, interviews and reports), the site's structural pages, the media library, and the D
  name: ODNI Public Content API
  slug: odni-public-content-api
artifact_total: 7
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/director-of-national-intelligence-wp-content-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/director-of-national-intelligence-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/director-of-national-intelligence-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/director-of-national-intelligence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/director-of-national-intelligence-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/director-of-national-intelligence-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/director-of-national-intelligence-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/director-of-national-intelligence-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/director-of-national-intelligence-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/director-of-national-intelligence-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/director-of-national-intelligence-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/director-of-national-intelligence-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/director-of-national-intelligence-wp-content-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/director-of-national-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.odni.gov/
- group: company
  title: ''
  type: Blog
  url: https://www.odni.gov/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.odni.gov/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.odni.gov/policies/
- group: operate
  title: ''
  type: Support
  url: https://www.odni.gov/get-in-touch/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/odni
created: '2024-07-11'
description: The Office of the Director of National Intelligence (ODNI) leads intelligence integration across the United States Intelligence Community. The DNI serves as head of the IC, principal intelligence adviser to the President, and oversees and coordinates the foreign and domestic activities of the 18 IC elements. ODNI houses the National Counterterrorism Center, the National Counterintelligence and Security Center, the Office of Economic Security and Emerging Technologies, the Mission Integration and Policy & Capabilities directorates, and the IC Inspector General. ODNI publishes no developer program and no machine-readable specification of its own; its public content — newsroom press releases, remarks, interviews, the Annual Threat Assessment, the annual IC transparency reports, IC directives and NCTC counterterrorism guides — is served from a WordPress site at www.odni.gov whose REST API answers anonymously and is catalogued here.
examples:
- key_count: 9
  name: Director Of National Intelligence Taxonomies
  slug: director-of-national-intelligence-taxonomies
- key_count: 16
  name: Director Of National Intelligence Types
  slug: director-of-national-intelligence-types
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/director-of-national-intelligence.png
layout: provider
modified: '2026-09-06'
name: Director of National Intelligence
nav: Providers
network: true
overview: 'Director of National Intelligence publishes 1 API on the [APIs.io](https://apis.io/) network: ODNI Public Content API. Tagged areas include Federal-Government, Intelligence, National-Security, Government, and Public-Sector.


  Director of National Intelligence''s developer surface includes authentication, engineering blog, support, and 18 more developer resources.'
plans:
- name: Director Of National Intelligence Plans Pricing
  plan_count: 0
  slug: director-of-national-intelligence-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Director Of National Intelligence Rate Limits
  slug: director-of-national-intelligence-rate-limits
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 16.5
    developer_ergonomics: 13.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 2.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/director-of-national-intelligence/refs/heads/main/screenshots/director-of-national-intelligence-2026-06-20T180032.png
security:
- kind: authentication
  name: Director Of National Intelligence Authentication
  slug: director-of-national-intelligence-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Director Of National Intelligence Domain Security
  slug: director-of-national-intelligence-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: director-of-national-intelligence
tags:
- Federal-Government
- Intelligence
- National-Security
- Government
- Public-Sector
- Transparency
- News
- Publications
website: https://www.odni.gov/
---
