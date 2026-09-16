---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-09-15'
api_count: 3
apis:
- baseURL: https://www.ai-model.jp/wp-json
  baseurl_source: declared
  description: 'The published roster of AI-generated models and AI talent that AI model markets to apparel and e-commerce clients, served anonymously as the "models" custom post type on the WordPress REST API behind '
  name: AI model Models API
  slug: aimodel-models-api
- baseURL: https://www.ai-model.jp/wp-json
  baseurl_source: declared
  description: Company news, recruitment posts, announcements, pages, the media library, categories and site-wide search, served anonymously by the WordPress REST API behind www.ai-model.jp.
  name: AI model Content API
  slug: aimodel-content-api
- baseURL: https://www.ai-model.jp/wp-json
  baseurl_source: declared
  description: Self-describing metadata for the public www.ai-model.jp WordPress REST API - registered content types, taxonomies and post statuses - and the route discovery document this profile was derived from.
  name: AI model Discovery API
  slug: aimodel-discovery-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.ai-model.jp/
- group: company
  title: ''
  type: Blog
  url: https://www.ai-model.jp/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ai-model.jp/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.ai-model.jp/contact/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.ai-model.jp/wp/wp-content/themes/aimodel/pdfs/ai-model_policy.pdf
- group: auth
  title: ''
  type: InformationSecurityPolicy
  url: https://www.ai-model.jp/wp/wp-content/themes/aimodel/pdfs/security_policy.pdf
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aimodel/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/authentication/aimodel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aimodel-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/conventions/aimodel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aimodel-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/errors/aimodel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aimodel-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/data-model/aimodel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aimodel-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/lifecycle/aimodel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aimodel-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/conformance/aimodel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aimodel-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/security/aimodel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimodel-domain-security.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/rate-limits/aimodel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aimodel-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/plans/aimodel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aimodel-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/packages/aimodel-packages.yml
  title: ''
  type: Packages
  url: packages/aimodel-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/mcp/aimodel-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aimodel-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/llms/aimodel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimodel-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aimodel/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-14'
description: 'AI model株式会社 (AI model Inc.) is a Tokyo generative-AI company, founded in August 2020 and headquartered in the Sumitomo Fudosan Toranomon Tower, Minato-ku, that generates and licenses photorealistic AI models and AI talent for apparel, e-commerce and advertising imagery. Its service replaces conventional model photography for product shots (ささげ), key visuals, lookbooks, television commercials, outdoor advertising and in-store POP, and it co-developed the AI character MirAI with Canon Marketing Japan. Its November 2024 Series A was backed by SBI Investment, NTT Docomo Ventures, the Canon Marketing Japan MIRAI Fund with Global Brain, Mitsukoshi Isetan Innovations, Sazaby League and Mitsubishi UFJ Capital; EquityZen reports a pre-Series B round with SBI Investment and Canon MJ CVC as of January 2026. AI model sells a managed creative service, not software: it publishes no developer portal, no API reference, no pricing page, no SDKs and no terms of service, and api., docs., developer.,
  developers. and app. under ai-model.jp do not resolve. The one public, anonymous, machine-readable surface on its estate is the WordPress REST API behind www.ai-model.jp, which serves its published AI model roster (8 records), company news (39), pages, the media library and site-wide search - captured here as three derived OpenAPI documents.'
image: https://www.ai-model.jp/wp/wp-content/uploads/2022/03/MV.jpg
layout: provider
modified: '2026-09-14'
name: AI model
nav: Providers
network: true
overview: 'AI model publishes 3 APIs on the [APIs.io](https://apis.io/) network: Models API, Content API, and Discovery API. Tagged areas include Artificial Intelligence, Generative AI, Japan, E-Commerce, and Fashion.


  AI model''s developer surface includes engineering blog, support, authentication, and 17 more developer resources.'
plans:
- name: Aimodel Plans Pricing
  plan_count: 0
  slug: aimodel-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Aimodel Rate Limits
  slug: aimodel-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 13.6
    developer_ergonomics: 20.8
    discoverability: 81.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 17.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Aimodel Authentication
  slug: aimodel-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aimodel Domain Security
  slug: aimodel-domain-security
  summary_line: TLSv1.3
slug: aimodel
tags:
- Artificial Intelligence
- Generative AI
- Japan
- E-Commerce
- Fashion
- Apparel
- Advertising
- Marketing
- Content
- Digital Human
- Media
- WordPress
website: https://www.ai-model.jp/
---
