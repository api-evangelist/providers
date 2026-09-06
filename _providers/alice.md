---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Alice Agentic Access
  operation_count: 18
  slug: alice-agentic-access
  summary_line: 18 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.alice.io
  baseurl_source: declared
  description: Provides APIs to manage API key(s), including adding new keys, listing existing keys, and deleting keys.
  name: Alice api keys API
  slug: alice-api-keys-api
- baseURL: https://api.alice.io
  baseurl_source: declared
  description: Collection API Represents grouped entities. A collection is comprised of multiple items grouped together in a playlist, album, folder, group or channel on your platform. For example, a playlist of vid
  name: Alice collection API
  slug: alice-collection-api
- baseURL: https://api.alice.io
  baseurl_source: declared
  description: Content APIs Represents WHAT content was created on your platform, such as a post, comment, review, message, article or data. For example, a web page containing a video, a customer review of a product
  name: Alice content API
  slug: alice-content-api
- baseURL: https://api.alice.io
  baseurl_source: declared
  description: The Flags API enables you to send details about the flag made on an item on your platform to the Alice T&S platform.
  name: Alice flags API
  slug: alice-flags-api
- baseURL: https://api.alice.io
  baseurl_source: declared
  description: Users API Represents WHO created content on your platform. These are the end users that have uploaded content to your platform, meaning the people who are the creators or publishers of the content. Fo
  name: Alice users API
  slug: alice-users-api
- baseURL: https://api.alice.io
  baseurl_source: declared
  description: WonderBuild provides red teaming and security assessment tools for AI applications. APIs for running comprehensive security assessments on gen-AI applications.
  name: Alice WonderBuild API
  slug: alice-wonderbuild-api
- baseURL: https://api.alice.io
  baseurl_source: declared
  description: 'WonderFence provides real-time guardrails for AI-generated content. APIs for evaluating and moderating AI-generated content and interactions to protect against harmful outputs and prompt attacks. ## A'
  name: Alice WonderFence API
  slug: alice-wonderfence-api
artifact_total: 19
asyncapis:
- description: ''
  name: Alice Webhooks
  slug: alice-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alice API Documentation api keys API
  slug: open-alice-api-keys-api
- collection_type: open
  name: Alice API Documentation collection API
  slug: open-alice-collection-api
- collection_type: open
  name: Alice API Documentation content API
  slug: open-alice-content-api
- collection_type: open
  name: Alice API Documentation flags API
  slug: open-alice-flags-api
- collection_type: open
  name: Alice API Documentation users API
  slug: open-alice-users-api
- collection_type: open
  name: Alice API Documentation WonderBuild API
  slug: open-alice-wonderbuild-api
- collection_type: open
  name: Alice API Documentation WonderFence API
  slug: open-alice-wonderfence-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/alice-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alice.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.alice.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.alice.io/reference
- group: company
  title: ''
  type: Blog
  url: https://alice.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alice.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alice.io/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alice-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/alice-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alice-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alice-domain-security.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/alice-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/alice-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alice-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alice-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alice-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alice-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alice-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/alice-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/alice-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alice-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://alice.io/
created: '2026-07-17'
description: Alice (formerly ActiveFence) is an enterprise AI security, safety, and trust platform for the GenAI era. Its WonderSuite platform stress-tests, guards, and monitors AI models, applications, and agents against jailbreaks, prompt injection, unsafe outputs, and policy violations. The Alice API provides content analysis (text, image, video, and audio moderation), real-time GenAI message evaluation (WonderFence), and adversarial red-team assessments (WonderBuild), authenticated with an af-api-key header and delivering asynchronous results via callback webhooks. Alice safeguards more than 3 billion users across 120+ languages and is SOC 2 and ISO 27001 certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alice.png
layout: provider
modified: '2026-07-17'
name: Alice
nav: Providers
network: true
overview: 'Alice publishes 7 APIs on the [APIs.io](https://apis.io/) network, including api keys API, collection API, content API, and 4 more. Tagged areas include Company, Developer Tools, AI Security, AI Safety, and Content Moderation.


  The Alice catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Alice''s developer surface includes documentation, API reference, engineering blog, authentication, and 19 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 66.1
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alice/refs/heads/main/screenshots/alice-2026-07-25T195611.png
security:
- kind: authentication
  name: Alice Authentication
  slug: alice-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alice Domain Security
  slug: alice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alice
tags:
- Company
- Developer Tools
- AI Security
- AI Safety
- Content Moderation
- Trust and Safety
- LLM Guardrails
- Red Teaming
- GenAI
website: https://alice.io/
---
