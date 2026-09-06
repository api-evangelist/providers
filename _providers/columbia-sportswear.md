---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Columbia Sportswear's partner-facing API platform, hosted on Microsoft Azure API Management. The portal at columbia.developer.azure-api.net lists API products, offers a try-it console, and takes subsc
  name: Columbia Sportswear Digital Developer Portal
  slug: digital-developer-portal
- baseURL: https://api.columbia.com/ContentHubExternal
  baseurl_source: declared
  description: 'Columbia Sportswear''s ContentHub image service for external customers. A read-only API with two GET operations: look up product imagery ("seasonal assets") for a single 10-digit material number, or pa'
  name: Content Hub External API
  slug: content-hub-external
artifact_total: 8
common:
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
  title: ''
  type: Authentication
  url: authentication/columbia-sportswear-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/columbia-sportswear-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/columbia-sportswear-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/columbia-sportswear-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/columbia-sportswear-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/columbia-sportswear-content-hub-external-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/columbia-sportswear-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/columbia-sportswear-mcp.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/columbia-sportswear-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/columbia-sportswear-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/columbia-sportswear-rate-limits.yml
created: '2025-03-23'
description: 'Columbia Sportswear is a global designer, marketer, and distributor of outdoor, active, and everyday lifestyle apparel, footwear, accessories, and equipment under the Columbia, Mountain Hardwear, SOREL, and prAna brands. Columbia Sportswear Digital runs a partner-facing API estate on Microsoft Azure API Management: a developer portal at columbia.developer.azure-api.net and a production gateway on Columbia''s own domain at api.columbia.com. Exactly one API product is documented anonymously - ContentHub External, a read-only product-imagery service with a published OpenAPI 3.0.1 contract - and every other product on the portal requires sign-in. Access is a partner arrangement rather than a developer program: subscriptions require Columbia''s approval, portal terms restrict use to Columbia employees and to vendors serving Columbia under agreement, and no price, rate limit, SLA or status page is published. The company also exchanges traditional EDI documents (POs, ASNs, invoices)
  with retail trading partners through providers like TrueCommerce and eZCom.'
finops:
- name: Columbia Sportswear Finops
  service_category: Retail
  slug: columbia-sportswear-finops
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
overview: 'Columbia Sportswear publishes 1 API on the [APIs.io](https://apis.io/) network: Content Hub External API. Tagged areas include Apparel, B2B, Consumer Management, Content Management, and Digital Asset Management.


  The Columbia Sportswear catalog on APIs.io includes 1 JSON-LD context.


  Columbia Sportswear''s developer surface includes API reference, signup flow, support, authentication, and 22 more developer resources.'
plans:
- name: Columbia Sportswear Plans Pricing
  plan_count: 1
  slug: columbia-sportswear-plans-pricing
press:
- date: '2026-05-25'
  title: The risk and benefit of brands using AI is closer than you ...
  url: https://www.prdaily.com/the-daily-scoop-the-risk-and-benefit-of-brands-using-ai-is-closer-than-you-think/
- date: '2026-05-25'
  title: As AI increases at Columbia Sportswear, so does the threat ...
  url: https://www.itbrew.com/stories/2023/10/04/as-ai-increases-at-columbia-sportswear-so-does-the-threat-surface
- date: '2026-05-25'
  title: 'Customer Story: Columbia'
  url: https://www.databricks.com/customers/columbia
- date: '2026-05-25'
  title: Columbia Sportswear's brand anthem inspires AI ...
  url: https://www.linkedin.com/posts/greg-balkin_genai-feels-a-bit-overwhelming-and-its-activity-7374904393676050432-kbEt
- date: '2026-05-25'
  title: Columbia Sportswear Company Advances Its Succession ...
  url: https://via.tt.se/pressmeddelande/4139504/columbia-sportswear-company-advances-its-succession-plans-and-appoints-co-presidents-peter-j-bragdon-and-joseph-p-boyle?publisherId=259167&lang=en
random_paper: 8
rate_limits:
- limit_count: 0
  name: Columbia Sportswear Rate Limits
  slug: columbia-sportswear-rate-limits
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 8.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 31.9
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 55.8
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 19.7
    operational_transparency: 2.6
  previous_composite: 13.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/columbia-sportswear/refs/heads/main/screenshots/columbia-sportswear-2026-06-20T174800.png
security:
- kind: authentication
  name: Columbia Sportswear Authentication
  slug: columbia-sportswear-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Columbia Sportswear Domain Security
  slug: columbia-sportswear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- Partner APIs
- Product Imagery
- Retail
website: https://www.columbia.com/
---
