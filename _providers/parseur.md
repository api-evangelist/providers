---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Parseur Agentic Access
  operation_count: 29
  slug: parseur-agentic-access
  summary_line: 29 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.parseur.com
  baseurl_source: declared
  description: The async API from Parseur — 7 operation(s) for async.
  name: Parseur async API
  slug: parseur-async-api
- baseURL: https://api.parseur.com
  baseurl_source: declared
  description: The Bootstrap API from Parseur — 1 operation(s) for bootstrap.
  name: Parseur Bootstrap API
  slug: parseur-bootstrap-api
- baseURL: https://api.parseur.com
  baseurl_source: declared
  description: The Document API from Parseur — 3 operation(s) for document.
  name: Parseur Document API
  slug: parseur-document-api
- baseURL: https://api.parseur.com
  baseurl_source: declared
  description: The Parser API from Parseur — 8 operation(s) for parser.
  name: Parseur Parser API
  slug: parseur-parser-api
- baseURL: https://api.parseur.com
  baseurl_source: declared
  description: The Template API from Parseur — 1 operation(s) for template.
  name: Parseur Template API
  slug: parseur-template-api
- baseURL: https://api.parseur.com
  baseurl_source: declared
  description: The Webhook API from Parseur — 2 operation(s) for webhook.
  name: Parseur Webhook API
  slug: parseur-webhook-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Parseur async API
  slug: open-parseur-async-api
- collection_type: open
  name: Parseur async Bootstrap API
  slug: open-parseur-bootstrap-api
- collection_type: open
  name: Parseur async Document API
  slug: open-parseur-document-api
- collection_type: open
  name: Parseur async Parser API
  slug: open-parseur-parser-api
- collection_type: open
  name: Parseur async Template API
  slug: open-parseur-template-api
- collection_type: open
  name: Parseur async Webhook API
  slug: open-parseur-webhook-api
- collection_type: open
  name: Parseur
  slug: open-parseur
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parseur-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parseur-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parseur-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parseur-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://parseur.com
- group: start
  title: ''
  type: Portal
  url: https://app.parseur.com
- group: start
  title: ''
  type: Signup
  url: https://app.parseur.com/accounts/signup/
- group: start
  title: ''
  type: Login
  url: https://app.parseur.com/accounts/login/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.parseur.com/
- group: operate
  title: ''
  type: SupportCenter
  url: https://help.parseur.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.parseur.com/openapi.json
- group: auth
  title: ''
  type: APIKeys
  url: https://app.parseur.com/account/api-keys
- group: company
  title: ''
  type: About
  url: https://parseur.com/about
- group: company
  title: ''
  type: Blog
  url: https://parseur.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://parseur.com/pricing
- group: operate
  title: ''
  type: Contact
  url: https://parseur.com/contact
- group: company
  title: ''
  type: Careers
  url: https://parseur.com/jobs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parseur.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://parseur.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://help.parseur.com/en/articles/4578268-security-and-privacy-at-parseur
- group: operate
  title: ''
  type: StatusPage
  url: https://status.parseur.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/parseur
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/parseur
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parseur.com
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@parseur
- group: other
  title: ''
  type: Reddit
  url: https://www.reddit.com/r/Parseur/
- group: commercial
  title: ''
  type: Plans
  url: https://parseur.com/pricing
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.parseur.com/
created: '2026-05-25'
description: Parseur is an AI-powered document and email parsing platform headquartered in Singapore that automatically extracts structured data from PDFs, emails, scanned documents, and arbitrary file uploads, then routes the resulting JSON, CSV, or Excel records into downstream systems via webhooks, native integrations, or its REST API. The platform combines Vision AI, Text AI, template-based extraction, OCR, normalization, and field validation behind a forwarding email address per mailbox, and connects to more than 1,000 applications including Zapier, Make, n8n, Power Automate, Google Sheets, Airtable, Salesforce, Excel, and Slack. Parseur exposes a public REST API at https://api.parseur.com with an OpenAPI 3.1 specification covering mailbox (parser) management, document upload and lifecycle, templates, custom export configurations, and webhook subscriptions, secured with a per-account Token-based Authorization header. Pricing is volume-based on pages processed, with a permanent free
  tier (20 pages/month) and Base, Scale, and Enterprise tiers that scale up to 10 million pages per month.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parseur.png
layout: provider
modified: '2026-05-25'
name: Parseur
nav: Providers
network: true
overview: 'Parseur publishes 6 APIs on the [APIs.io](https://apis.io/) network, including async API, Bootstrap API, Document API, and 3 more. Tagged areas include Artificial Intelligence, Document Parsing, Document Processing, Document Extraction, and Email Parsing.


  Parseur''s developer surface includes authentication, developer portal, signup flow, documentation, engineering blog, pricing, GitHub presence, and 21 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parseur/refs/heads/main/screenshots/parseur-2026-06-20T191421.png
security:
- kind: authentication
  name: Parseur Authentication
  slug: parseur-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Parseur Domain Security
  slug: parseur-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Parseur Vulnerability Disclosure
  slug: parseur-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: parseur
tags:
- Artificial Intelligence
- Document Parsing
- Document Processing
- Document Extraction
- Email Parsing
- OCR
- Data Extraction
- Vision AI
- Automation
- Webhook
- Mailboxes
- Software-as-a-Service
website: https://parseur.com
---
