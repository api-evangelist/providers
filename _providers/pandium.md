---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 33.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Pandium Agentic Access
  operation_count: 14
  slug: pandium-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 2
apis:
- baseURL: https://api.pandium.io
  baseurl_source: declared
  description: Proxy calls to external APIs on behalf of a tenant.
  name: Pandium Connector Calls API
  slug: pandium-connector-calls-api
- baseURL: https://api.pandium.io
  baseurl_source: declared
  description: Manage integrations on the Pandium platform.
  name: Pandium Integrations API
  slug: pandium-integrations-api
- baseURL: https://api.pandium.io
  baseurl_source: declared
  description: View run status and trigger syncs.
  name: Pandium Runs API
  slug: pandium-runs-api
- baseURL: https://api.pandium.io
  baseurl_source: declared
  description: Manage metadata associated with tenants.
  name: Pandium Tenant Metadata API
  slug: pandium-tenant-metadata-api
- baseURL: https://api.pandium.io
  baseurl_source: declared
  description: Manage tenants (customer instances of integrations).
  name: Pandium Tenants API
  slug: pandium-tenants-api
- baseURL: https://api.pandium.io
  baseurl_source: declared
  description: Create builds for integrations from source control; a build can then be used to create a release.
  name: Pandium Builds API
  slug: pandium-builds-api
artifact_total: 236
asyncapis:
- description: ''
  name: Pandium Webhooks
  slug: pandium-webhooks
collections:
- collection_type: postman
  name: Pandium Connector Calls API
  slug: postman-pandium-connector-calls-api
- collection_type: postman
  name: Pandium Connector Calls Integrations API
  slug: postman-pandium-integrations-api
- collection_type: postman
  name: Pandium Connector Calls Runs API
  slug: postman-pandium-runs-api
- collection_type: postman
  name: Pandium Connector Calls Tenant Metadata API
  slug: postman-pandium-tenant-metadata-api
- collection_type: postman
  name: Pandium Connector Calls Tenants API
  slug: postman-pandium-tenants-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pandium Connector Calls API
  slug: open-pandium-connector-calls-api
- collection_type: open
  name: Pandium Connector Calls Integrations API
  slug: open-pandium-integrations-api
- collection_type: open
  name: Pandium API
  slug: open-pandium-pandium
- collection_type: open
  name: Pandium Connector Calls Runs API
  slug: open-pandium-runs-api
- collection_type: open
  name: Pandium Connector Calls Tenant Metadata API
  slug: open-pandium-tenant-metadata-api
- collection_type: open
  name: Pandium Connector Calls Tenants API
  slug: open-pandium-tenants-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pandium/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pandium-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pandium-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pandium-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pandium-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pandium-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pandium
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pandium/
- group: other
  title: ''
  type: Customers
  url: https://www.pandium.com/customer-stories
- group: other
  title: ''
  type: eBooks
  url: https://www.pandium.com/ebooks
- group: company
  title: ''
  type: Blog
  url: https://www.pandium.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://www.pandium.com/faqs
- group: other
  title: ''
  type: Podcast
  url: https://www.pandium.com/podcast
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pandium.com/
- group: other
  title: ''
  type: Glossary
  url: https://docs.pandium.com/getting-started/key-terminology
- group: build
  title: ''
  type: CLI
  url: https://docs.pandium.com/getting-started/pandium-integration-development-kit-idk/pandium-cli
- group: other
  title: ''
  type: WhatsNew
  url: https://www.pandium.com/blog/product-updates
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pandium.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pandium.com/
- group: company
  title: ''
  type: Partners
  url: https://www.pandium.com/teams/partnerships
- group: auth
  title: ''
  type: Security
  url: https://www.pandium.com/security
- group: company
  title: ''
  type: Website
  url: https://www.pandium.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pandium.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pandium.com/privacy-policy
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.pandium.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/pandium-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/pandium-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pandium-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pandium-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pandium-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pandium-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pandium-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pandium-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/pandium-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pandium-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pandium-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/pandium-cli.yml
- group: design
  title: ''
  type: Components
  url: components/pandium-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pandium-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pandium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pandium-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pandium.com/reference/pandium-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pandium.com/getting-started/pandium-integration-tutorial
created: '2025-01-07'
description: Transform integration development from a fragmented, ad hoc process into a streamlined, repeatable workflow with Pandiums Integration Platform. With Pandium, B2B SaaS companies can meet customer demands, reduce technical debt, and stay ahead in an increasingly connected world.
features:
- name: Automated CI/CD
- name: CLI (Command Line Interface)
- name: Code-First Approach
- name: Comprehensive Reporting and Analytics
- name: Customizable In-App Marketplace (Optional)
- name: Extensive Connector Library
- name: Integration Development Kit (Idk)
- name: Integration Hub
- name: Managed Authentication
- name: Partner Portal
finops:
- name: Pandium Finops
  service_category: API
  slug: pandium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pandium.png
integrations:
- name: Activecampaign
- name: Afterpay
- name: Aftership
- name: Airship
- name: Algolia
- name: Amazon
- name: Ankored
- name: Apollo
- name: Appsignal
- name: Asknicely
- name: Assembled
- name: Attentive
- name: AWS
- name: Azure Service Bus
- name: Bandcamp
- name: Bazaarvoice
- name: Bigcommerce
- name: Bitbucket
- name: Booker
- name: Box
- name: Braze
- name: Brightpearl
- name: Campaign Monitor
- name: Capabl
- name: Chargebee
- name: null
- name: Chargify
- name: Chubb
- name: CIN7
- name: Coach Packet
- name: Constant Contact
- name: Customer Thermometer
- name: Datadog
- name: Datev
- name: Delighted
- name: Dhl
- name: Domo
- name: Dotdigital
- name: Drip
- name: Dropbox
- name: Dynamicyield
- name: E-Tip
- name: Easyship
- name: Eloqua
- name: Emotive
- name: Endear
- name: Envision
- name: Envision Cloud
- name: Evaluagent
- name: Exact Online
- name: Ezcom
- name: Fabric
- name: Facebook
- name: falcon.io
- name: Famer
- name: FedEx
- name: Field Nation
- name: Finch
- name: Fivetran
- name: Fleetio
- name: Flowcode
- name: Follow Up Boss
- name: Foundation Software
- name: Fulfil
- name: Getresponse
- name: Github
- name: Gitlab
- name: Gladly
- name: Google
- name: Gooten
- name: Gorgias
- name: Greenhouse
- name: Handshake
- name: Happy Returns
- name: Hootsuite
- name: Hubspot
- name: Image Relay
- name: Imgur
- name: Iterable
- name: Jasper
- name: Jdp
- name: Justuno
- name: Klaus
- name: Klaviyo
- name: Kombo
- name: Kontent by Kentico
- name: Kustomer
- name: Kvcore
- name: Leagueapps
- name: Lessonly
- name: Lexoffice
- name: Linga
- name: Linnworks
- name: Listrak
- name: Loop Returns
- name: Lucid Travel
- name: Lytx
- name: Maestroqa
- name: Magento
- name: Magento 2
- name: Mailchimp
- name: Marketo
- name: Medallia
- name: Microsoft Cloud
- name: Microsoft Dynamics 365
- name: Microsoft Entra
- name: Mintsoft
- name: Ncsa
- name: Netomi
- name: Netsuite
- name: Nicereply
- name: Nylas
- name: Omnisend
- name: Onpay
- name: Onramp
- name: Ontraport
- name: Optimizely
- name: Paycom
- name: Personio
- name: Perspective
- name: Players Health
- name: Playvox
- name: Pleo
- name: Postscript
- name: promoter.io
- name: Qualtrics
- name: Quickbooks
- name: Recart
- name: Recharge
- name: Recurly
- name: Returnly
- name: Reverselogix
- name: Rydership
- name: Sage
- name: Sage Intacct
- name: Sailthru
- name: Salesforce
- name: Salesforce Marketing Cloud
- name: Salesforce Pardot
- name: Sendgrid
- name: Sendlane
- name: Sevenrooms
- name: Shipbob
- name: Shiphero
- name: Shipmonk
- name: Shippo
- name: Shipstation
- name: Shopify
- name: Skubana
- name: Slack
- name: Smartrmail
- name: Smartrr
- name: smile.io
- name: Solidus
- name: Springbig
- name: Square
- name: Stamped
- name: Stella Connect
- name: Sugarcrm
- name: Swell
- name: Talkable
- name: Teamgenius
- name: Tether
- name: Thankful
- name: TikTok
- name: Tradegecko
- name: Trinet
- name: Triple Whale
- name: Trustpilot
- name: Twilio
- name: Twitter
- name: Unbabel
- name: UPS
- name: Upscribe
- name: USPS
- name: Visma
- name: Visma E-conomic
- name: Walmart
- name: Whiplash
- name: Wix
- name: Xero
- name: Yardstik
- name: Yotpo
- name: Zendesk
- name: Zingtree
- name: Zonos
json_schemas:
- name: Pandium Integration
  property_count: 5
  slug: integration
- name: Pandium Release
  property_count: 5
  slug: release
- name: Pandium Run
  property_count: 9
  slug: run
- name: Pandium Tenant
  property_count: 14
  slug: tenant
jsonld:
- class_count: 0
  name: Pandium Context
  property_count: 4
  slug: pandium-context
layout: provider
modified: '2026-09-03'
name: Pandium
nav: Providers
network: true
overview: 'Pandium publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Connector Calls API, Integrations API, Runs API, and 3 more. Tagged areas include B2B, Hub, Integration, Workflows, and iPaaS.


  The Pandium catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Pandium''s developer surface includes authentication, engineering blog, FAQ, documentation, CLI, pricing, sandbox, and 37 more developer resources.'
plans:
- name: Pandium Plans Pricing
  plan_count: 2
  slug: pandium-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Pandium Rate Limits
  slug: pandium-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pandium API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pandium-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 66.3
    catalog_earned_first_party: 8.0
    catalog_gap: 48.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 14.4
    contract_quality: 71.5
    developer_ergonomics: 65.5
    discoverability: 75.9
    governance: 14.4
    operational_transparency: 55.3
  previous_composite: 61.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 16.7
      total: 6
    mcp: derived
    skills: unknown
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pandium/refs/heads/main/screenshots/pandium-2026-06-20T191334.png
security:
- kind: authentication
  name: Pandium Authentication
  slug: pandium-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pandium Domain Security
  slug: pandium-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pandium Vulnerability Disclosure
  slug: pandium-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Pandium Trust Center
  slug: pandium-trust-center
  summary_line: SOC 2
slug: pandium
tags:
- B2B
- Hub
- Integration
- Workflows
- iPaaS
use_cases:
- name: Building and Launching User-Facing Integrations
- name: Enhanced Customer Experience
- name: In-App Marketplace Infrastructure
- name: Reduced Engineering Costs and Effort
- name: Revenue Generation
- name: Scalability and Flexibility
- name: Simplified Integration Management
website: https://www.pandium.com/
---
