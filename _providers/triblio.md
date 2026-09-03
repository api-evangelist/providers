---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://foundryco.com/our-solutions/software-q2/
- group: other
  title: ''
  type: Parent
  url: https://foundryco.com
- group: other
  title: ''
  type: Product
  url: https://foundryco.com/our-solutions/account-based-marketing/
- group: other
  title: ''
  type: IntentData
  url: https://foundryco.com/our-solutions/data/intent-data/
- group: other
  title: ''
  type: Advertising
  url: https://foundryco.com/our-solutions/advertising/
- group: other
  title: ''
  type: WebPersonalization
  url: https://foundryco.com/our-solutions/website-visitor-tracking/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://learning.foundryco.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://learning.foundryco.com/hc/en-us
- group: other
  title: ''
  type: HubSpotMarketplace
  url: https://ecosystem.hubspot.com/marketplace/apps/triblio
- group: build
  title: ''
  type: BomboraIntegration
  url: https://bombora.com/integration/triblio/
- group: company
  title: ''
  type: Blog
  url: https://foundryco.com/blog/
- group: company
  title: ''
  type: Press
  url: https://foundryco.com/press/
- group: company
  title: ''
  type: Careers
  url: https://foundryco.com/work-here/
- group: operate
  title: ''
  type: Contact
  url: https://foundryco.com/contact-us/
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://foundryco.com/blog/idg-acquires-triblio-heres-why-it-matters/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foundryco.com/terms-of-service-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foundryco.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://foundryco.com/about-us/privacy-compliance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/triblio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triblio
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/triblio
- group: build
  title: ''
  type: Packages
  url: packages/triblio-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/triblio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/triblio-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triblio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/triblio-llms.txt
coverage:
  checked: '2026-08-12'
  detail: The Triblio brand has been fully absorbed into Foundry and its entire web surface decommissioned — triblio.com is still registered to MarkMonitor and delegated to four Route 53 nameservers, but those nameservers answer REFUSED because the hosted zone was deleted, so the marketing site, the application at app.triblio.com and the knowledge base at learning.triblio.com all fail DNS resolution; the product now ships as "Foundry ABM, powered by Triblio" and Foundry's only developer portal documents the KickFire APIs, a different product, which must not be attributed here.
  evidence:
  - status: 0
    url: https://www.triblio.com
  - status: 0
    url: https://learning.triblio.com/
  - status: 503
    url: https://intent.foundryco.com/login
  - status: 403
    url: https://learning.foundryco.com/hc/en-us
  - status: 200
    url: https://foundryco.com/our-solutions/software-q2/
  - status: 200
    url: https://foundryco.com/developers/
  reason: defunct
  state: none
created: '2026-05-25'
description: 'Triblio is an account-based marketing (ABM) platform now owned by Foundry, the marketing services and data unit of International Data Group (IDG). Originally founded in Reston, Virginia, Triblio was acquired by IDG/Foundry in June 2020 as the cornerstone of a multi-year strategy to combine first- party publisher data, third-party intent signals, and ABM advertising, web personalization, and sales acceleration into a single platform. The product combines account-based advertising, intent-driven audience segmentation, website personalization, and a Smart Score that ranks accounts using behavioral signals from first-party web visits, third-party intent providers (notably Bombora Company Surge and G2 intent), CRM data, and Foundry''s own publisher network. Triblio integrates with major CRMs and marketing automation systems including Salesforce, HubSpot, Microsoft Dynamics 365, SugarCRM, Marketo, Pardot, LinkedIn Campaign Manager, Google Analytics, and Slack. Foundry positions Triblio
  as the engine behind its broader Sales Acceleration and Foundry ABM offerings, with intent data feeds from Bombora ingested weekly and G2 intent ingested nightly. Triblio does not publish a public developer API portal, OpenAPI specification, or open-source SDKs; the GitHub organization at github.com/triblio was archived in January 2026 with no public repos. Customer integrations are delivered through pre-built CRM and MAP connectors, an Apps Marketplace, and platform-internal automation rather than a self-serve developer API. As of a 2026-08-12 probe the Triblio brand has no web surface of its own: triblio.com remains registered to MarkMonitor through 2027 but its Route 53 hosted zone has been deleted, so the marketing site, the app.triblio.com login, and the learning.triblio.com knowledge base all fail DNS resolution. The product now ships as "Foundry ABM, powered by Triblio" at foundryco.com, and the knowledge base has moved to learning.foundryco.com — a Cloudflare-fronted CNAME to triblio.zendesk.com.
  Foundry''s sole developer portal covers the KickFire APIs, a different Foundry product, and is not attributed to Triblio.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/triblio.png
layout: provider
modified: '2026-08-12'
name: Triblio
nav: Providers
network: true
overview: 'Triblio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Account Based Marketing, Advertising, Intent Data, Marketing Technology, and MarTech.


  Triblio''s developer surface includes support, engineering blog, and 24 more developer resources.'
plans:
- name: Triblio Plans Pricing
  plan_count: 0
  slug: triblio-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Triblio Rate Limits
  slug: triblio-rate-limits
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triblio/refs/heads/main/screenshots/triblio-2026-06-20T195708.png
security:
- kind: domain-security
  name: Triblio Domain Security
  slug: triblio-domain-security
  summary_line: no transport/DNS hardening detected
slug: triblio
tags:
- Account Based Marketing
- Advertising
- Intent Data
- Marketing Technology
- MarTech
- B2B Marketing
- Sales Acceleration
- Web Personalization
- Audience Segmentation
- Demand Generation
- CRM Integration
- Foundry
- IDG
website: https://foundryco.com/our-solutions/software-q2/
---
