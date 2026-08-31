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
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cataas Agentic Access
  operation_count: 15
  slug: cataas-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 4
apis:
- description: Administrative operations on the cat catalog (admin token required)
  name: Cataas Admin API
  slug: cataas-admin-api
- description: Browse cats, tags, and stats programmatically (JSON)
  name: Cataas Catalog API
  slug: cataas-catalog-api
- description: Random and tagged cat image retrieval
  name: Cataas Cats API
  slug: cataas-cats-api
- description: Submit a cat image (rate-limited / moderated)
  name: Cataas Upload API
  slug: cataas-upload-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cataas Admin API
  slug: open-cataas-admin-api
- collection_type: open
  name: Cataas Admin Catalog API
  slug: open-cataas-catalog-api
- collection_type: open
  name: Cataas Admin Cats API
  slug: open-cataas-cats-api
- collection_type: open
  name: Cataas Admin Upload API
  slug: open-cataas-upload-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cataas/cataas/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cataas-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cataas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cataas-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cataas.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cataas
- group: build
  title: Canonical Cataas server (Node.js)
  type: GitHubRepository
  url: https://github.com/cataas/cataas
- group: build
  title: Cataas Discord bot
  type: GitHubRepository
  url: https://github.com/cataas/discord-bot
- group: build
  title: Cataas Slack slash command
  type: GitHubRepository
  url: https://github.com/cataas/slack-command
- group: build
  title: Cataas image editor library
  type: GitHubRepository
  url: https://github.com/cataas/image-editor
- group: build
  title: MCP Server (community via Pipeworx Gateway)
  type: Tools
  url: https://github.com/pipeworx-io/mcp-cataas
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/cataas-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cataas-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cataas-context.jsonld
created: '2026-05-28'
description: Cataas (Cat as a Service) is a free, open-source REST API that returns random cat images and GIFs with optional tags, filters, sizing, and text overlays. The service is widely embedded in tutorials, demos, README files, and chat applications as a friction-free image source. The canonical implementation lives at github.com/cataas/cataas and runs at cataas.com.
examples:
- key_count: 9
  name: Cat Example
  slug: cat-example
- key_count: 1
  name: Count Response Example
  slug: count-response-example
- key_count: 1
  name: Edit Cat Request Example
  slug: edit-cat-request-example
- key_count: 2
  name: Upload Cat Request Example
  slug: upload-cat-request-example
features:
- description: GET /cat returns a random cat image (JPEG, PNG, or GIF).
  name: Random Cat Image
- description: GET /cat/{tag} returns a random cat matching one or more comma-separated tags.
  name: Tagged Cat Retrieval
- description: GET /cat/gif returns a random animated cat.
  name: Animated GIFs
- description: GET /cat/says/{text} renders user-supplied text on top of a random cat with configurable font size, color, and background.
  name: Text Overlay
- description: filter=blur|mono|negate|custom with per-channel and per-property tuning (brightness, hue, saturation, RGB).
  name: Image Filters
- description: type, width, height, fit, and position query parameters resize and crop the returned image.
  name: Sizing and Cropping
- description: /api/cats, /api/tags, /api/count expose the catalog programmatically.
  name: JSON Catalog API
- description: json=true returns a metadata document instead of binary; html=true returns an embedding wrapper page.
  name: Content Negotiation
- description: All read endpoints are public and require no API key.
  name: Free and Unauthenticated
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cataas.png
integrations:
- description: Official slack-command repo wires /cat into Slack workspaces.
  name: Slack
- description: Official discord-bot repo provides a Cataas Discord integration.
  name: Discord
- description: Community MCP server (pipeworx-io/mcp-cataas) wraps the API for use by Claude and other MCP clients.
  name: Pipeworx MCP Gateway
- description: Listed in the public-apis/public-apis Animals category.
  name: Public APIs Catalog
json_schemas:
- name: Cat
  property_count: 9
  slug: cat
- name: CountResponse
  property_count: 1
  slug: count-response
- name: EditCatRequest
  property_count: 1
  slug: edit-cat-request
- name: UploadCatRequest
  property_count: 2
  slug: upload-cat-request
json_structures:
- name: Cat Structure
  property_count: 9
  slug: cat-structure
- name: Count Response Structure
  property_count: 1
  slug: count-response-structure
- name: Edit Cat Request Structure
  property_count: 1
  slug: edit-cat-request-structure
- name: Upload Cat Request Structure
  property_count: 2
  slug: upload-cat-request-structure
jsonld:
- class_count: 4
  name: Cataas Context
  property_count: 11
  slug: cataas-context
layout: provider
modified: '2026-05-30'
name: Cataas
nav: Providers
network: true
overview: 'Cataas publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Catalog API, Cats API, and 1 more. Tagged areas include Animals, Cats, Image, Open-Source, and Public APIs.


  The Cataas catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cataas'' developer surface includes authentication, tooling, and 13 more developer resources.'
random_paper: 12
rules:
- effective_rule_count: 5
  extends: []
  name: Cataas API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cataas-jsonschema-spectral-rules
- effective_rule_count: 81
  extends:
  - spectral:oas
  name: Cataas API Rules
  rule_count: 40
  severity_counts:
    error: 12
    hint: 0
    info: 4
    warn: 24
  slug: cataas-spectral-rules
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 29.2
    developer_ergonomics: 38.1
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 2.6
  previous_composite: 26.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cataas/refs/heads/main/screenshots/cataas-2026-06-20T174040.png
security:
- kind: authentication
  name: Cataas Authentication
  slug: cataas-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cataas Domain Security
  slug: cataas-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cataas
solutions:
- description: Run your own Cataas instance from cataas/cataas (Node.js + MongoDB + sharp) to power internal demos or branded image services.
  name: Self-Hosted Catalog
tags:
- Animals
- Cats
- Image
- Open-Source
- Public APIs
use_cases:
- description: Embed live cat images in API tutorials, learn-to-code lessons, and conference demos.
  name: Tutorials and Demos
- description: Decorate open-source READMEs and personal sites with rotating cat imagery.
  name: README Decoration
- description: Slack, Discord, and Teams bots fetch random cats on demand via /cat or /cat/says.
  name: Chat Bots and Slash Commands
- description: Stand in for a real image-CDN-backed API while prototyping front-end layouts.
  name: Mocking Image-Heavy APIs
- description: Exercise resize, format-conversion, and filtering pipelines with predictable image input.
  name: Image Pipeline Testing
website: https://cataas.com/
---
