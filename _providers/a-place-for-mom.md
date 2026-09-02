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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The integration surface of You''ve Got Leads, the senior-living CRM that is a division of A Place for Mom, Inc. The public integrations page names an "application programming interface (API)" used for '
  name: You've Got Leads API
  slug: a-place-for-mom-youve-got-leads-api
artifact_total: 5
asyncapis:
- description: ''
  name: A Place For Mom Webhooks
  slug: a-place-for-mom-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.aplaceformom.com/
- group: company
  title: ''
  type: About
  url: https://www.aplaceformom.com/about
- group: operate
  title: ''
  type: Support
  url: https://support.aplaceformom.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.aplaceformom.com/docs/for-care-providers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aplaceformom.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aplaceformom.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aplaceformom
- group: company
  title: ''
  type: Careers
  url: https://www.aplaceformom.com/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/a-place-for-mom-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/a-place-for-mom-support-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/a-place-for-mom-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/a-place-for-mom-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/a-place-for-mom-domain-security.yml
coverage:
  checked: '2026-08-10'
  detail: 'A Place for Mom does operate an API — its You''ve Got Leads division advertises an API and webhooks on a public page and runs a live host at api.youvegotleads.com — but every route to the contract ends at a person: youvegotleads.com/api 302s to a login, the integrations page closes with "Contact us now" to support@youvegotleads.com, and the public help center returns zero articles for "API".'
  evidence:
  - status: 302
    url: https://www.youvegotleads.com/api
  - status: 200
    url: https://www.youvegotleads.com/ygl-Integrations
  - status: 404
    url: https://api.youvegotleads.com/openapi.json
  - status: 200
    url: https://ygl.zendesk.com/api/v2/help_center/articles/search.json?query=API
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: A Place for Mom is North America's largest senior living referral service, connecting families with assisted living, memory care, independent living, home care, and other senior care options through a network of Senior Living Advisors and a large marketplace of care communities. Families use the service at no cost to search, compare, and get matched to providers, while care communities and home care agencies partner with A Place for Mom to receive and manage referral leads, respond to and moderate consumer reviews, and track billing and performance through provider-facing portals. A Place for Mom was surfaced as a portfolio company of Battery Ventures and Insight Partners and added to the API Evangelist network for enrichment. The company operates consumer-facing web properties plus provider, community-partner, reputation, and home care portals, and publishes a support knowledge base (including an llms.txt documentation index) rather than a public developer API program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/a-place-for-mom.png
layout: provider
modified: '2026-08-10'
name: A Place for Mom
nav: Providers
network: true
overview: 'A Place for Mom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Senior Living, Senior Care, Referral Marketplace, and Home Care.


  The A Place for Mom catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  A Place for Mom''s developer surface includes support and 12 more developer resources.'
plans:
- name: A Place For Mom Plans Pricing
  plan_count: 0
  slug: a-place-for-mom-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: A Place For Mom Rate Limits
  slug: a-place-for-mom-rate-limits
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 4.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/a-place-for-mom/refs/heads/main/screenshots/a-place-for-mom-2026-07-25T181304.png
security:
- kind: domain-security
  name: A Place For Mom Domain Security
  slug: a-place-for-mom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: a-place-for-mom
tags:
- Company
- Senior Living
- Senior Care
- Referral Marketplace
- Home Care
- Healthcare
- Reviews
- Lead Generation
website: https://www.aplaceformom.com/
---
