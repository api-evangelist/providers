---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Columbia Sportswear's partner-facing API platform, hosted on Microsoft Azure API Management. The portal at columbia.developer.azure-api.net lists API products, offers a try-it console, and takes subsc
  name: Columbia Sportswear Digital Developer Portal
  slug: digital-developer-portal
- baseURL: https://api.columbia.com/
  baseurl_source: declared
  description: The ExternalImage API from Columbia Sportswear — 2 operation(s) for externalimage.
  name: Columbia Sportswear External Image API
  slug: columbia-sportswear-externalimage-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/columbia-sportswear/finops/columbia-sportswear-finops.yml
  title: ''
  type: FinOps
  url: finops/columbia-sportswear-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.columbia.com/
- group: other
  title: ''
  type: Corporate
  url: https://www.columbiasportswear.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://columbia.developer.azure-api.net/
- group: docs
  title: ''
  type: APIReference
  url: https://columbia.developer.azure-api.net/apis
- group: start
  title: ''
  type: SignUp
  url: https://columbia.developer.azure-api.net/signup
- group: operate
  title: ''
  type: Support
  url: https://help.columbia.com/s/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/columbiasportswear
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/columbia-sportswear
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.columbia.com/t/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.columbia.com/t/legal/terms-of-use/
- group: company
  title: ''
  type: Investor Relations
  url: https://investor.columbia.com/
- group: other
  title: ''
  type: Mountain Hardwear
  url: https://www.mountainhardwear.com/
- group: other
  title: ''
  type: SOREL
  url: https://www.sorel.com/
- group: other
  title: ''
  type: prAna
  url: https://www.prana.com/
- group: auth
  href: https://artifacts.apis.io/columbia-sportswear/authentication/columbia-sportswear-authentication.yml
  title: ''
  type: Authentication
  url: authentication/columbia-sportswear-authentication.yml
- group: auth
  href: https://artifacts.apis.io/columbia-sportswear/security/columbia-sportswear-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/columbia-sportswear-domain-security.yml
- group: design
  href: https://artifacts.apis.io/columbia-sportswear/conventions/columbia-sportswear-conventions.yml
  title: ''
  type: Conventions
  url: conventions/columbia-sportswear-conventions.yml
- group: design
  href: https://artifacts.apis.io/columbia-sportswear/lifecycle/columbia-sportswear-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/columbia-sportswear-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/columbia-sportswear/packages/columbia-sportswear-packages.yml
  title: ''
  type: Packages
  url: packages/columbia-sportswear-packages.yml
- group: other
  href: https://artifacts.apis.io/columbia-sportswear/overlays/columbia-sportswear-content-hub-external-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/columbia-sportswear-content-hub-external-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/columbia-sportswear/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/columbia-sportswear/llms/columbia-sportswear-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/columbia-sportswear-llms.txt
- group: agent
  href: https://artifacts.apis.io/columbia-sportswear/mcp/columbia-sportswear-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/columbia-sportswear-mcp.yml
- group: design
  href: https://artifacts.apis.io/columbia-sportswear/vocabulary/columbia-sportswear-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/columbia-sportswear-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/columbia-sportswear/plans/columbia-sportswear-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/columbia-sportswear-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/columbia-sportswear/rate-limits/columbia-sportswear-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/columbia-sportswear-rate-limits.yml
created: '2025-03-23'
description: 'Columbia Sportswear is a global designer, marketer, and distributor of outdoor, active, and everyday lifestyle apparel, footwear, accessories, and equipment under the Columbia, Mountain Hardwear, SOREL, and prAna brands. Columbia Sportswear Digital runs a partner-facing API estate on Microsoft Azure API Management: a developer portal at columbia.developer.azure-api.net and a production gateway on Columbia''s own domain at api.columbia.com. Exactly one API product is documented anonymously - ContentHub External, a read-only product-imagery service with a published OpenAPI 3.0.1 contract - and every other product on the portal requires sign-in. Access is a partner arrangement rather than a developer program: subscriptions require Columbia''s approval, portal terms restrict use to Columbia employees and to vendors serving Columbia under agreement, and no price, rate limit, SLA or status page is published. The company also exchanges traditional EDI documents (POs, ASNs, invoices)
  with retail trading partners through providers like TrueCommerce and eZCom.'
finops:
- has_sources: true
  method: derived
  name: Columbia Sportswear Finops
  primary_unit: ''
  service_category: ''
  slug: columbia-sportswear-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/columbia-sportswear.png
jsonld:
- class_count: 50
  name: Columbia Sportswear Context
  property_count: 9
  slug: columbia-sportswear-context
layout: provider
modified: '2026-09-05'
name: Columbia Sportswear
nav: Providers
network: true
overview: 'Columbia Sportswear publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including External Image API, and 1 more. Tagged areas include Apparel, B2B, Consumer Management, Content Management, and Digital Asset Management.


  The Columbia Sportswear catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Columbia Sportswear''s developer surface includes API reference, signup flow, support, authentication, and 23 more developer resources.'
plans:
- name: Columbia Sportswear Plans Pricing
  plan_count: 1
  slug: columbia-sportswear-plans-pricing
press:
- date: ''
  title: The risk and benefit of brands using AI is closer than you ...
  url: https://www.prdaily.com/the-daily-scoop-the-risk-and-benefit-of-brands-using-ai-is-closer-than-you-think/
- date: ''
  title: As AI increases at Columbia Sportswear, so does the threat ...
  url: https://www.itbrew.com/stories/2023/10/04/as-ai-increases-at-columbia-sportswear-so-does-the-threat-surface
- date: ''
  title: 'Customer Story: Columbia'
  url: https://www.databricks.com/customers/columbia
- date: ''
  title: Columbia Sportswear's brand anthem inspires AI ...
  url: https://www.linkedin.com/posts/greg-balkin_genai-feels-a-bit-overwhelming-and-its-activity-7374904393676050432-kbEt
- date: ''
  title: Columbia Sportswear Company Advances Its Succession ...
  url: https://via.tt.se/pressmeddelande/4139504/columbia-sportswear-company-advances-its-succession-plans-and-appoints-co-presidents-peter-j-bragdon-and-joseph-p-boyle?publisherId=259167&lang=en
random_paper: 11
rate_limits:
- limit_count: 0
  name: Columbia Sportswear Rate Limits
  slug: columbia-sportswear-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Columbia Sportswear API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: columbia-sportswear-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.0
    catalog_earned_first_party: 8.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 53.8
    developer_ergonomics: 44.6
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 45.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/columbia-sportswear/columbia-sportswear-2026-06-20T174800.png
security:
- kind: authentication
  name: Columbia Sportswear Authentication
  slug: columbia-sportswear-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Columbia Sportswear Domain Security
  slug: columbia-sportswear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: columbia-sportswear-product-imagery-sync
  slug: columbia-sportswear-product-imagery-sync
slug: columbia-sportswear
tags:
- Apparel
- B2B
- Consumer Management
- Content Management
- Digital Asset Management
- Footwear
- Fortune 1000
- Outdoor
- Partner API
- Product Imagery
- Retail
- Fashion
website: https://www.columbia.com/
---
