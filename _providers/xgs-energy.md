---
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Xgs Energy Agentic Access
  operation_count: 17
  slug: xgs-energy-agentic-access
  summary_line: 17 operations
api_count: 8
apis:
- baseURL: https://www.xgsenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the XGS Energy news and insights archive via the WordPress core REST API. Verified live at 108 published posts on 2026-09-04.
  name: XGS Energy Posts API
  slug: xgs-energy-posts-api
- baseURL: https://www.xgsenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the static marketing and policy pages of xgsenergy.com. Verified live at 8 published pages on 2026-09-04.
  name: XGS Energy Pages API
  slug: xgs-energy-pages-api
- baseURL: https://www.xgsenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the media library behind xgsenergy.com. Verified live at 182 attachments on 2026-09-04.
  name: XGS Energy Media API
  slug: xgs-energy-media-api
- baseURL: https://www.xgsenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated cross-content search over xgsenergy.com, returning lightweight id / title / url / type / subtype records. Verified live at 127 searchable objects on 2026-09-04.
  name: XGS Energy Search API
  slug: xgs-energy-search-api
- baseURL: https://www.xgsenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated access to the post categories that classify the XGS Energy news archive. Verified live at 4 categories on 2026-09-04.
  name: XGS Energy Categories API
  slug: xgs-energy-categories-api
- baseURL: https://www.xgsenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated access to the post tags applied to the XGS Energy news archive. Verified live at 1 tag on 2026-09-04.
  name: XGS Energy Tags API
  slug: xgs-energy-tags-api
- baseURL: https://www.xgsenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated discovery metadata for xgsenergy.com — the self-describing route index (266 routes across 21 namespaces at capture), the registered content types, taxonomies and publication st
  name: XGS Energy Discovery API
  slug: xgs-energy-discovery-api
- baseURL: https://www.xgsenergy.com/wp-json
  baseurl_source: declared
  description: Public oEmbed 1.0 provider endpoint for xgsenergy.com URLs, returning embeddable rich metadata — provider, author, title, dimensions and iframe HTML — for any post or page.
  name: XGS Energy oEmbed API
  slug: xgs-energy-oembed-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.xgsenergy.com/
- group: company
  title: ''
  type: About
  url: https://www.xgsenergy.com/team/
- group: company
  title: ''
  type: Blog
  url: https://www.xgsenergy.com/news-and-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.xgsenergy.com/news-and-insights/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.xgsenergy.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.xgsenergy.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://www.xgsenergy.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xgsenergy.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xgsenergy.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xgs-energy
- group: build
  title: ''
  type: Packages
  url: packages/xgs-energy-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/xgs-energy-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/xgs-energy-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xgs-energy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xgs-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xgs-energy-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/xgs-energy-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xgs-energy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xgs-energy-lifecycle.yml
created: '2026-09-04'
description: 'XGS Energy is a next-generation geothermal power developer founded in 2008 and headquartered in Palo Alto, California, formerly Geothermic Solution. Its patented Thermal Reach Enhancement technology packs a thermally conductive material around a closed-loop wellbore so heat is drawn from the surrounding rock without relying on natural permeability or produced water, siting geothermal in geology conventional hydrothermal and EGS cannot use. It is developing a 150 MW round-the-clock project in New Mexico with Meta and utility PNM, and in 2025 acquired drilling firm Capuano Engineering. XGS Energy is an energy infrastructure developer, not a software vendor: it publishes no developer program, product API, SDKs or API documentation. The only machine-readable interface it exposes is the WordPress REST content API behind www.xgsenergy.com, captured here for discovery — anonymously readable, read-only, and undocumented by the company.'
image: https://www.xgsenergy.com/wp-content/uploads/2024/08/cropped-favicon-192x192.png
layout: provider
modified: '2026-09-04'
name: XGS Energy
nav: Providers
network: true
overview: 'XGS Energy publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 5 more. Tagged areas include Company, Energy, Geothermal, Renewable Energy, and Clean Energy.


  XGS Energy''s developer surface includes engineering blog, support, and 18 more developer resources.'
plans:
- name: Xgs Energy Plans Pricing
  plan_count: 0
  slug: xgs-energy-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Xgs Energy Rate Limits
  slug: xgs-energy-rate-limits
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 12.9
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Xgs Energy Authentication
  slug: xgs-energy-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Xgs Energy Domain Security
  slug: xgs-energy-domain-security
  summary_line: TLSv1.3
slug: xgs-energy
tags:
- Company
- Energy
- Geothermal
- Renewable Energy
- Clean Energy
- Power Generation
- Energy Infrastructure
- Data Center Power
- Climate Tech
- Content
website: https://www.xgsenergy.com/
---
