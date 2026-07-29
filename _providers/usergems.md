---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Usergems Agentic Access
  operation_count: 5
  slug: usergems-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 3
apis:
- description: Add and remove accounts UserGems should source prospects against.
  name: UserGems Accounts API
  slug: usergems-accounts-api
- description: Add and remove contacts UserGems should track for job changes.
  name: UserGems Contacts API
  slug: usergems-contacts-api
- description: Honor data-subject deletion requests for tracked contacts.
  name: UserGems Privacy API
  slug: usergems-privacy-api
artifact_total: 49
collections:
- collection_type: postman
  name: UserGems Accounts API
  slug: postman-usergems-accounts-api
- collection_type: postman
  name: UserGems Accounts Contacts API
  slug: postman-usergems-contacts-api
- collection_type: postman
  name: UserGems Accounts Privacy API
  slug: postman-usergems-privacy-api
- collection_type: open
  name: UserGems API
  slug: open-usergems-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/usergems/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usergems-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/usergems-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/usergems-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usergems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usergems-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.usergems.com
- group: start
  title: ''
  type: Portal
  url: https://www.usergems.com/product
- group: docs
  title: ''
  type: Documentation
  url: https://app.usergems.com/api/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com/article/usergems-implementation-guide-salesforce-crm
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com/article/usergems-implementation-guide-hubspot-crm
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com/article/how-many-salesforce-api-calls-does-usergems-use
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com/article/usergems-outreach-configuration
- group: other
  title: ''
  type: Product
  url: https://www.usergems.com/product/api
- group: start
  title: ''
  type: Signup
  url: https://www.usergems.com/demo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usergems.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.usergems.com/blog
- group: other
  title: ''
  type: Customers
  url: https://www.usergems.com/customers
- group: company
  title: ''
  type: Careers
  url: https://www.usergems.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.usergems.com/contact
- group: operate
  title: ''
  type: Support
  url: mailto:support@usergems.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usergems.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usergems.com/legal/terms
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.usergems.com/security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usergems
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/usergems
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usergems
- group: commercial
  title: ''
  type: Plans
  url: plans/usergems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usergems-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usergems-finops.yml
created: '2026-05-25'
description: UserGems is a San Francisco-based sales intelligence platform that tracks champion job changes and surfaces buying signals so sales and marketing teams can prioritize outbound and ABM motions. The platform packages 30+ native signals (job changes, contact-level intent, M&A, hiring, web visits), Gem-E AI agents for prospect list building and email personalization, and custom AI scoring trained on 600+ closed-won patterns. UserGems exposes a public REST API at api.usergems.com/v1 that lets customers programmatically add and remove contacts to track for job changes, add and remove target accounts, and honor data-subject deletion requests. The API uses an X-Api-Key header for authentication and processes submissions asynchronously. Native integrations include Salesforce, HubSpot, Microsoft Dynamics, Outreach, Salesloft, Gong Engage, Marketo, LinkedIn Ads, Meta Ads, and Google Ads.
examples:
- key_count: 6
  name: Usergems Add Account Example
  slug: usergems-add-account-example
- key_count: 8
  name: Usergems Add Contact Example
  slug: usergems-add-contact-example
- key_count: 1
  name: Usergems Privacy Delete Example
  slug: usergems-privacy-delete-example
features:
- Gem-E AI agents for prospect list building and email personalization
- 30+ native signals (job changes, contact-level intent, hiring, M&A, web visits)
- Custom AI scoring trained on 600+ closed-won patterns
- Intelligent workflows orchestrating ads, outreach, and CRM updates
- Contact-level intent (specific buyers, not just account-level)
- Outbound REST API for contact and account submission with up to 100 custom signal fields per contact
- Privacy delete endpoint for GDPR/CCPA right-to-erasure
- X-Api-Key header authentication
- Asynchronous queue-based processing
- Customer-configurable Salesforce API cap (default 20K calls per 24h per instance)
- Native integrations with Salesforce, HubSpot, Dynamics, Outreach, Salesloft, Gong, Marketo, LinkedIn/Meta/Google Ads
- Chrome extension for in-workflow access
- SOC 2 Type 2, GDPR, and CCPA compliance posture
- Money-back ROI guarantee — $100K spend tied to $100K pipeline
finops:
- name: Usergems Finops
  service_category: Sales Intelligence and ABM
  slug: usergems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usergems.png
integrations:
- category: CRM
  name: Salesforce
- category: CRM
  name: HubSpot
- category: CRM
  name: Microsoft Dynamics
- category: Sales Engagement
  name: Outreach
- category: Sales Engagement
  name: Salesloft
- category: Sales Engagement
  name: Gong Engage
- category: Marketing Automation
  name: HubSpot Marketing
- category: Marketing Automation
  name: Marketo
- category: Advertising
  name: LinkedIn Ads
- category: Advertising
  name: Meta Ads
- category: Advertising
  name: Google Ads
- category: Productivity
  name: Chrome Extension
json_schemas:
- name: UserGems Account
  property_count: 7
  slug: usergems-account
- name: UserGems Contact
  property_count: 9
  slug: usergems-contact
jsonld:
- class_count: 0
  name: Usergems Context
  property_count: 3
  slug: usergems-context
layout: provider
modified: '2026-05-25'
name: UserGems
nav: Providers
network: true
overview: 'UserGems publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Contacts API, and Privacy API. Tagged areas include Sales Intelligence, Outbound, ABM, Champion Tracking, and Job Changes.


  The UserGems catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  UserGems'' developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, support, and 24 more developer resources.'
plans:
- name: Usergems Plans Pricing
  plan_count: 1
  slug: usergems-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 4
  name: Usergems Rate Limits
  slug: usergems-rate-limits
rules:
- name: UserGems API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: usergems-jsonschema-spectral-rules
- name: UserGems API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: usergems-rules
score:
  band: strong
  composite: 59.3
  delta: -3.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 78.0
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usergems/refs/heads/main/screenshots/usergems-2026-06-20T200715.png
security:
- kind: authentication
  name: Usergems Authentication
  slug: usergems-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Usergems Domain Security
  slug: usergems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Usergems Vulnerability Disclosure
  slug: usergems-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Usergems Trust Center
  slug: usergems-trust-center
  summary_line: SOC 2, GDPR
slug: usergems
tags:
- Sales Intelligence
- Outbound
- ABM
- Champion Tracking
- Job Changes
- Buying Signals
- AI Scoring
- Sales Engagement
- CRM
- Revenue Operations
- GTM
website: https://www.usergems.com
---
