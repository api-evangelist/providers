---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Two live Model Context Protocol servers registered under the `mcp` REST namespace on engrail.com, fronted by RFC 8414 and RFC 9728 OAuth discovery documents at the apex. Both are OAuth-protected — ano
  name: Engrail Therapeutics MCP Servers
  slug: mcp
- description: 'The public WordPress REST API (wp-json) of the Engrail Therapeutics website at www.engrail.com: the route index of the site''s content management system, catalogued as one site surface rather than as s'
  name: Engrail Therapeutics Website (WordPress REST)
  slug: engrail-com-website-wordpress-rest
artifact_total: 9
collections:
- collection_type: open
  name: Engrail Therapeutics Site Content API (WordPress REST)
  slug: open-engrail-therapeutics-content
common:
- group: other
  href: https://artifacts.apis.io/engrail-therapeutics/overlays/engrail-therapeutics-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/engrail-therapeutics-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.engrail.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/engrail-therapeutics_stock/
- group: company
  title: ''
  type: About
  url: https://www.engrail.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.engrail.com/investors-media/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.engrail.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.engrail.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.engrail.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.engrail.com/privacy-policy/
- group: commercial
  title: ''
  type: LegalDisclaimer
  url: https://www.engrail.com/legal-disclaimer/
- group: company
  title: ''
  type: Careers
  url: https://www.engrail.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://www.engrail.com/partners/
- group: other
  title: ''
  type: Pipeline
  url: https://www.engrail.com/pipeline/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/engrail-therapeutics
- group: agent
  href: https://artifacts.apis.io/engrail-therapeutics/well-known/engrail-therapeutics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/engrail-therapeutics-well-known.yml
- group: auth
  href: https://artifacts.apis.io/engrail-therapeutics/authentication/engrail-therapeutics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/engrail-therapeutics-authentication.yml
- group: auth
  href: https://artifacts.apis.io/engrail-therapeutics/scopes/engrail-therapeutics-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/engrail-therapeutics-scopes.yml
- group: design
  href: https://artifacts.apis.io/engrail-therapeutics/conventions/engrail-therapeutics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/engrail-therapeutics-conventions.yml
- group: design
  href: https://artifacts.apis.io/engrail-therapeutics/conformance/engrail-therapeutics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/engrail-therapeutics-conformance.yml
- group: design
  href: https://artifacts.apis.io/engrail-therapeutics/lifecycle/engrail-therapeutics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/engrail-therapeutics-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/engrail-therapeutics/security/engrail-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/engrail-therapeutics-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/engrail-therapeutics/llms/engrail-therapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/engrail-therapeutics-llms.txt
- group: agent
  href: https://artifacts.apis.io/engrail-therapeutics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/engrail-therapeutics/errors/engrail-therapeutics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/engrail-therapeutics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/engrail-therapeutics/data-model/engrail-therapeutics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/engrail-therapeutics-data-model.yml
created: '2026-08-01'
description: Engrail Therapeutics is a clinical-stage precision-neuroscience pharmaceutical company founded in 2019 and headquartered in San Diego, California. It applies precision chemistry and pharmacology to scientifically validated mechanisms of action, developing targeted small-molecule therapies for neuropsychiatric and neurodevelopmental diseases with significant unmet need — including generalized anxiety disorder, major depressive disorder characterized by anhedonia, post-traumatic stress disorder and rare neurodegenerative conditions. Its lead program, ENX-102, is a highly selective GABA-A alpha-2,3,5 positive allosteric modulator in Phase 2 (the ENCALM trial) for generalized anxiety disorder; ENX-104 is in clinical development for anhedonic depression. The company closed an oversubscribed $157M Series B in March 2024 co-led by F-Prime Capital, Forbion and Norwest Venture Partners, bringing total capital raised since inception past $220M. Engrail publishes no product or developer
  API; the machine-readable surfaces catalogued here are the public read-only content API and the OAuth-protected Model Context Protocol servers exposed by its corporate website.
image: https://www.engrail.com/wp-content/uploads/2022/05/logo.png
layout: provider
mcp_servers:
- description: 'engrail.com runs two live Model Context Protocol servers on its WordPress-backed corporate site, registered under the `mcp` REST namespace and fronted by RFC 8414 / RFC 9728 OAuth discovery documents '
  name: Engrail Therapeutics MCP Server
  slug: engrail-therapeutics-mcp-yml
modified: '2026-08-01'
name: Engrail Therapeutics
nav: Providers
network: true
overview: 'Engrail Therapeutics is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Neuroscience.


  Engrail Therapeutics'' developer surface includes engineering blog, support, authentication, and 22 more developer resources.'
random_paper: 16
scopes:
- name: Engrail Therapeutics Scopes
  scope_count: 1
  slug: engrail-therapeutics-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 1.7
    developer_ergonomics: 25.6
    discoverability: 60.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 22.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/engrail-therapeutics/engrail-therapeutics-2026-08-07T164922.png
security:
- kind: authentication
  name: Engrail Therapeutics Authentication
  slug: engrail-therapeutics-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Engrail Therapeutics Domain Security
  slug: engrail-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Read Engrail Therapeutics company news
  slug: engrail-therapeutics-read-company-news
- name: Search and map Engrail Therapeutics site content
  slug: engrail-therapeutics-search-site-content
slug: engrail-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Neuroscience
- Clinical Trials
- Drug Development
- Healthcare
- Mental Health
- MCP
website: https://www.engrail.com/
---
