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
    auth_clarity: bearer
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The Impact API lets developers programmatically fund climate impact on behalf of an Ecologi account. POST endpoints purchase trees, local trees in specific countries (UK, US, AU, BR), carbon avoidance
  name: Ecologi Impact API
  slug: ecologi-impact-api
- description: The Reporting API exposes read-only impact totals for any public Ecologi account by username. GET endpoints return total trees funded, CO2e avoided, CO2e removed, habitat restored, and a combined impa
  name: Ecologi Reporting API
  slug: ecologi-reporting-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ecologi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecologi-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://ecologi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ecologi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://ecologi.com/impact-api
- group: start
  title: ''
  type: Signup
  url: https://ecologi.com/pay-as-you-go
- group: start
  title: ''
  type: Signup
  url: https://ecologi.com/impact-api
- group: operate
  title: ''
  type: Support
  url: https://help.ecologi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.ecologi.com/api-automation-overview
- group: docs
  title: ''
  type: Documentation
  url: https://help.ecologi.com/api-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://help.ecologi.com/ecologi-api-and-integration-pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://ecologi.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://help.ecologi.com/ecologi-api-and-integration-pricing
- group: company
  title: ''
  type: Blog
  url: https://ecologi.com/articles
- group: company
  title: ''
  type: Newsroom
  url: https://ecologi.com/articles
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecologi.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecologi.com/terms
- group: company
  title: ''
  type: About
  url: https://ecologi.com/about
- group: other
  title: ''
  type: Business
  url: https://ecologi.com/business
- group: other
  title: ''
  type: Projects
  url: https://ecologi.com/projects
- group: other
  title: ''
  type: ImpactLedger
  url: https://ecologi.com/projects
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ecologi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ecologi/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ecologi_hq
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/ecologi/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ecologi
- group: operate
  title: ''
  type: Contact
  url: https://ecologi.com/contact
- group: company
  title: ''
  type: Careers
  url: https://ecologi.com/careers
created: '2026-05-24'
description: Ecologi is a Bristol, UK climate action platform and B Corp founded in 2019 that lets individuals and businesses fund verified reforestation, carbon avoidance, carbon removal, and habitat restoration projects through monthly subscriptions, pay-as-you-go purchases, and a public Impact API. The platform has funded over 95 million trees, avoided 4.1 million tonnes of CO2e, removed 61,000 tonnes of CO2e, and restored 102,000 square metres of habitat across projects in Guatemala, Brazil, Kenya, Uganda, India, Pakistan, the UK, and beyond. Ecologi serves over 16,000 businesses with an end-to-end Measure, Reduce, Report (3Rs) workflow aligned to SBTi, GHG Protocol, ISO 14064-1, SECR, and CSRD, and exposes a public REST API (and a Zapier app and Shopify app) so any business can automate climate impact per order, per signup, per invoice, or per workflow event. The Impact API supports trees, local trees (UK/US/AU/BR), carbon avoidance, carbon removal, and habitat restoration as programmable
  purchases, with bearer-token auth, test mode, and idempotency keys; a separate public Reporting API exposes any user account's impact totals without authentication for embedding climate-positive badges.
features:
- Public Impact API with five POST endpoints — trees, local-trees, carbon, carbon-removal, habitat-restoration
- Public Reporting API with five GET endpoints exposing per-user impact totals (refreshed every 10 minutes)
- Bearer-token authentication on the Impact API, no auth required on the Reporting API
- Test mode via "test": true for safe simulation without charges
- Idempotency-Key header support for safe automatic retries
- Recipient attribution on every purchase (name + recipientEmail) for gifting impact
- Local-tree planting in the UK, US, Australia, and Brazil
- Carbon purchases in KG or Tonnes units
- Permanent carbon-removal purchases backed by verified registries
- Habitat restoration purchases in square metres
- Zapier app (Plant Trees, Buy Carbon Offsets) connecting WooCommerce, Stripe, Mailchimp, and thousands of others
- Shopify app supporting per-product, per-order, percentage-of-order, and Shopify Flow triggers
- Monthly invoicing with a £3 minimum threshold
- Public Impact Ledger with verified registry links and certificates for every project
- 3Rs framework (Reduce, Restore, Report) aligned with SBTi, GHG Protocol, ISO 14064-1, SECR, and CSRD
- Carbon Project Assessment Framework (CPAF) and Nature Project Assessment Framework (NPAF)
- B Corp certified (top 5% for governance and environment) and B Corp of the Year at 2026 edie Awards
- Over 95M trees funded, 4.1M tonnes CO2e avoided, 61k tonnes CO2e removed, 102k m2 habitat restored
- Climate-positive badge and embeddable impact widgets for business websites
- End-to-end emissions measurement, reduction, and reporting for 16,000+ businesses
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecologi.png
layout: provider
modified: '2026-05-24'
name: Ecologi
nav: Providers
network: true
overview: 'Ecologi publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Climate, Climate Action, Carbon Offsets, Carbon Removal, and Carbon Avoidance.


  Ecologi''s developer surface includes developer portal, documentation, getting-started guide, signup flow, support, pricing, engineering blog, and 21 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecologi/refs/heads/main/screenshots/ecologi-2026-06-20T180444.png
security:
- kind: domain-security
  name: Ecologi Domain Security
  slug: ecologi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ecologi Vulnerability Disclosure
  slug: ecologi-vulnerability-disclosure
  summary_line: disclosure policy published
slug: ecologi
tags:
- Climate
- Climate Action
- Carbon Offsets
- Carbon Removal
- Carbon Avoidance
- Reforestation
- Tree Planting
- Habitat Restoration
- Sustainability
- ESG
- Net Zero
- B Corp
- Impact
- Verified Carbon
- Reporting
- Zapier
- Shopify
- Webhook
website: https://ecologi.com
---
