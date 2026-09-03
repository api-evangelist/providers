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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.0
  scored_at: '2026-09-02'
api_count: 11
apis:
- description: Two live Model Context Protocol servers registered under the `mcp` REST namespace on engrail.com, fronted by RFC 8414 and RFC 9728 OAuth discovery documents at the apex. Both are OAuth-protected — ano
  name: Engrail Therapeutics MCP Servers
  slug: mcp
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Categories API from Engrail Therapeutics — 2 operation(s) for categories.
  name: Engrail Therapeutics Categories API
  slug: engrail-therapeutics-categories-api
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Comments API from Engrail Therapeutics — 2 operation(s) for comments.
  name: Engrail Therapeutics Comments API
  slug: engrail-therapeutics-comments-api
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Media API from Engrail Therapeutics — 2 operation(s) for media.
  name: Engrail Therapeutics Media API
  slug: engrail-therapeutics-media-api
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Pages API from Engrail Therapeutics — 2 operation(s) for pages.
  name: Engrail Therapeutics Pages API
  slug: engrail-therapeutics-pages-api
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Posts API from Engrail Therapeutics — 2 operation(s) for posts.
  name: Engrail Therapeutics Posts API
  slug: engrail-therapeutics-posts-api
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Search API from Engrail Therapeutics — 1 operation(s) for search.
  name: Engrail Therapeutics Search API
  slug: engrail-therapeutics-search-api
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Statuses API from Engrail Therapeutics — 1 operation(s) for statuses.
  name: Engrail Therapeutics Statuses API
  slug: engrail-therapeutics-statuses-api
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Tags API from Engrail Therapeutics — 2 operation(s) for tags.
  name: Engrail Therapeutics Tags API
  slug: engrail-therapeutics-tags-api
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Taxonomies API from Engrail Therapeutics — 1 operation(s) for taxonomies.
  name: Engrail Therapeutics Taxonomies API
  slug: engrail-therapeutics-taxonomies-api
- baseURL: https://www.engrail.com/wp-json
  baseurl_source: declared
  description: The Types API from Engrail Therapeutics — 1 operation(s) for types.
  name: Engrail Therapeutics Types API
  slug: engrail-therapeutics-types-api
artifact_total: 16
collections:
- collection_type: open
  name: Engrail Therapeutics Site Content API (WordPress REST)
  slug: open-engrail-therapeutics-content
common:
- group: other
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
  title: ''
  type: WellKnown
  url: well-known/engrail-therapeutics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/engrail-therapeutics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/engrail-therapeutics-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/engrail-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/engrail-therapeutics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/engrail-therapeutics-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/engrail-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/engrail-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: Engrail Therapeutics is a clinical-stage precision-neuroscience pharmaceutical company founded in 2019 and headquartered in San Diego, California. It applies precision chemistry and pharmacology to scientifically validated mechanisms of action, developing targeted small-molecule therapies for neuropsychiatric and neurodevelopmental diseases with significant unmet need — including generalized anxiety disorder, major depressive disorder characterized by anhedonia, post-traumatic stress disorder and rare neurodegenerative conditions. Its lead program, ENX-102, is a highly selective GABA-A alpha-2,3,5 positive allosteric modulator in Phase 2 (the ENCALM trial) for generalized anxiety disorder; ENX-104 is in clinical development for anhedonic depression. The company closed an oversubscribed $157M Series B in March 2024 co-led by F-Prime Capital, Forbion and Norwest Venture Partners, bringing total capital raised since inception past $220M. Engrail publishes no product or developer
  API; the machine-readable surfaces catalogued here are the public read-only content API and the OAuth-protected Model Context Protocol servers exposed by its corporate website.
image: https://www.engrail.com/wp-content/uploads/2022/05/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Engrail Therapeutics MCP Server
  slug: engrail-therapeutics-mcp-server
modified: '2026-08-01'
name: Engrail Therapeutics
nav: Providers
network: true
overview: 'Engrail Therapeutics publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Comments API, Media API, and 7 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Neuroscience.


  Engrail Therapeutics'' developer surface includes engineering blog, support, authentication, and 20 more developer resources.'
random_paper: 1
scopes:
- name: Engrail Therapeutics Scopes
  scope_count: 1
  slug: engrail-therapeutics-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 13.8
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/engrail-therapeutics/refs/heads/main/screenshots/engrail-therapeutics-2026-08-07T164922.png
security:
- kind: authentication
  name: Engrail Therapeutics Authentication
  slug: engrail-therapeutics-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Engrail Therapeutics Domain Security
  slug: engrail-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
