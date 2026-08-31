---
access_model:
  confidence: high
  label: No public API programme · institutional key on request
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication/university-of-amsterdam-authentication.yml
  - https://github.com/uva/UvA-HvA-Agentic-Tools
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The university's own SAML 2.0 identity provider, entity ID http://login.uva.nl/adfs/services/trust. Signed federation metadata is served from the institution's own host and the entity is registered in
  name: UvA Identity Provider (SAML 2.0 / SURFconext)
  slug: identity-federation
- description: DataNose is the course, registration, timetable and thesis-administration system used by the University of Amsterdam's Faculty of Science. Its API host resolves into UVANET1, the university's own RIPE
  name: DataNose API
  slug: datanose
- description: The University of Amsterdam Library publishes its digitised collections — books, letters, maps, images, audio, video, sheet music, archaeological objects and the Beeldbank image repository — as linked
  name: UvA Library Linked Open Data (TriplyDB tenancy)
  slug: lod-triply
- description: 'UvA-DARE, the university''s digital academic repository, and the research information system behind it run on Elsevier Pure: pure.uva.nl CNAMEs to uva.elsevierpure.com. The OAI-PMH provider answers Ide'
  name: UvA-DARE OAI-PMH and Pure Web Service (Elsevier Pure tenancy)
  slug: oai-pure-dare
- description: OAI-PMH provider exposing EAD collection descriptions and inventories from the University of Amsterdam Library archives and the Allard Pierson heritage collections, under PDDL. The host is a UvA subdo
  name: UvA Archives Collection Descriptions OAI-PMH (ArchivesSpace tenancy)
  slug: oai-archives
- description: The harvesting endpoint the university library documents for its central catalogue — roughly 2.5 million bibliographic records in MARC-XML and unqualified Dublin Core. It runs on the library's Ex Libr
  name: UvA Central Catalogue OAI-PMH (Ex Libris Alma tenancy)
  slug: oai-catalogue
- description: The shared research data repository of the University of Amsterdam and the Amsterdam University of Applied Sciences, running on Figshare at uvaauas.figshare.com. DOIs are minted under the institution'
  name: UvA/HvA Research Data Repository (Figshare tenancy)
  slug: research-data-figshare
- description: The university timetable at rooster.uva.nl exposes a JSON API under /api/ that answers 401 with a structured error to unauthenticated callers, so the surface is real and gated behind institutional sig
  name: UvA Timetable API (MyTimetable tenancy)
  slug: timetable
- description: The a2a API from University of Amsterdam — 5 operation(s) for a2a.
  name: University of Amsterdam A2a API
  slug: university-of-amsterdam-a2a-api
- description: The a2a_registration API from University of Amsterdam — 1 operation(s) for a2a_registration.
  name: University of Amsterdam A2a Registration API
  slug: university-of-amsterdam-a2a-registration-api
- description: The access group management API from University of Amsterdam — 4 operation(s) for access group management.
  name: University of Amsterdam access group management API
  slug: university-of-amsterdam-access-group-management-api
- description: The adaptive_router API from University of Amsterdam — 1 operation(s) for adaptive_router.
  name: University of Amsterdam Adaptive Router API
  slug: university-of-amsterdam-adaptive-router-api
- description: The Agent Management API from University of Amsterdam — 1 operation(s) for agent management.
  name: University of Amsterdam Agent Management API
  slug: university-of-amsterdam-agent-management-api
- description: The Agents API from University of Amsterdam — 1 operation(s) for agents.
  name: University of Amsterdam Agents API
  slug: university-of-amsterdam-agents-api
- description: The Anthropic Pass-through API from University of Amsterdam — 1 operation(s) for anthropic pass-through.
  name: University of Amsterdam Anthropic Pass-through API
  slug: university-of-amsterdam-anthropic-pass-through-api
- description: The anthropic_skills API from University of Amsterdam — 2 operation(s) for anthropic_skills.
  name: University of Amsterdam Anthropic Skills API
  slug: university-of-amsterdam-anthropic-skills-api
- description: The Apply Guardrail API from University of Amsterdam — 1 operation(s) for apply guardrail.
  name: University of Amsterdam Apply Guardrail API
  slug: university-of-amsterdam-apply-guardrail-api
- description: The AssemblyAI EU Pass-through API from University of Amsterdam — 1 operation(s) for assemblyai eu pass-through.
  name: University of Amsterdam AssemblyAI EU Pass-through API
  slug: university-of-amsterdam-assemblyai-eu-pass-through-api
- description: The AssemblyAI Pass-through API from University of Amsterdam — 1 operation(s) for assemblyai pass-through.
  name: University of Amsterdam AssemblyAI Pass-through API
  slug: university-of-amsterdam-assemblyai-pass-through-api
- description: The assistants API from University of Amsterdam — 12 operation(s) for assistants.
  name: University of Amsterdam Assistants API
  slug: university-of-amsterdam-assistants-api
- description: The audio API from University of Amsterdam — 4 operation(s) for audio.
  name: University of Amsterdam Audio API
  slug: university-of-amsterdam-audio-api
- description: The Audit Logging API from University of Amsterdam — 2 operation(s) for audit logging.
  name: University of Amsterdam Audit Logging API
  slug: university-of-amsterdam-audit-logging-api
- description: The Azure AI Pass-through API from University of Amsterdam — 1 operation(s) for azure ai pass-through.
  name: University of Amsterdam Azure AI Pass-through API
  slug: university-of-amsterdam-azure-ai-pass-through-api
- description: The Azure Pass-through API from University of Amsterdam — 1 operation(s) for azure pass-through.
  name: University of Amsterdam Azure Pass-through API
  slug: university-of-amsterdam-azure-pass-through-api
- description: The batch API from University of Amsterdam — 9 operation(s) for batch.
  name: University of Amsterdam Batch API
  slug: university-of-amsterdam-batch-api
- description: The Bedrock Pass-through API from University of Amsterdam — 1 operation(s) for bedrock pass-through.
  name: University of Amsterdam Bedrock Pass-through API
  slug: university-of-amsterdam-bedrock-pass-through-api
- description: The [beta] A2A Agents API from University of Amsterdam — 4 operation(s) for [beta] a2a agents.
  name: University of Amsterdam [beta] A2A Agents API
  slug: university-of-amsterdam-beta-a2a-agents-api
- description: The [beta] Agents API from University of Amsterdam — 2 operation(s) for [beta] agents.
  name: University of Amsterdam [beta] Agents API
  slug: university-of-amsterdam-beta-agents-api
- description: The [beta] Anthropic Event Logging API from University of Amsterdam — 1 operation(s) for [beta] anthropic event logging.
  name: University of Amsterdam [beta] Anthropic Event Logging API
  slug: university-of-amsterdam-beta-anthropic-event-logging-api
- description: The [beta] Anthropic Messages Token Counting API from University of Amsterdam — 1 operation(s) for [beta] anthropic messages token counting.
  name: University of Amsterdam [beta] Anthropic Messages Token Counting API
  slug: university-of-amsterdam-beta-anthropic-messages-token-counting-api
- description: The [beta] Anthropic `/v1/messages` API from University of Amsterdam — 1 operation(s) for [beta] anthropic `/v1/messages`.
  name: University of Amsterdam [beta] Anthropic `/v1/messages` API
  slug: university-of-amsterdam-beta-anthropic-v1-messages-api
- description: The [beta] MCP API from University of Amsterdam — 1 operation(s) for [beta] mcp.
  name: University of Amsterdam [beta] MCP API
  slug: university-of-amsterdam-beta-mcp-api
- description: The budget management API from University of Amsterdam — 6 operation(s) for budget management.
  name: University of Amsterdam budget management API
  slug: university-of-amsterdam-budget-management-api
- description: The Budget & Spend Tracking API from University of Amsterdam — 12 operation(s) for budget & spend tracking.
  name: University of Amsterdam Budget & Spend Tracking API
  slug: university-of-amsterdam-budget-spend-tracking-api
- description: The Cache Settings API from University of Amsterdam — 2 operation(s) for cache settings.
  name: University of Amsterdam Cache Settings API
  slug: university-of-amsterdam-cache-settings-api
- description: The caching API from University of Amsterdam — 4 operation(s) for caching.
  name: University of Amsterdam Caching API
  slug: university-of-amsterdam-caching-api
- description: The chat/completions API from University of Amsterdam — 4 operation(s) for chat/completions.
  name: University of Amsterdam Chat/completions API
  slug: university-of-amsterdam-chat-completions-api
- description: The Claude Code Marketplace API from University of Amsterdam — 6 operation(s) for claude code marketplace.
  name: University of Amsterdam Claude Code Marketplace API
  slug: university-of-amsterdam-claude-code-marketplace-api
- description: The Cohere Pass-through API from University of Amsterdam — 1 operation(s) for cohere pass-through.
  name: University of Amsterdam Cohere Pass-through API
  slug: university-of-amsterdam-cohere-pass-through-api
- description: The completions API from University of Amsterdam — 4 operation(s) for completions.
  name: University of Amsterdam Completions API
  slug: university-of-amsterdam-completions-api
- description: The compliance API from University of Amsterdam — 2 operation(s) for compliance.
  name: University of Amsterdam Compliance API
  slug: university-of-amsterdam-compliance-api
- description: The Config API from University of Amsterdam — 3 operation(s) for config.
  name: University of Amsterdam Config API
  slug: university-of-amsterdam-config-api
- description: The containers API from University of Amsterdam — 10 operation(s) for containers.
  name: University of Amsterdam Containers API
  slug: university-of-amsterdam-containers-api
- description: The Coordination Redis Settings API from University of Amsterdam — 2 operation(s) for coordination redis settings.
  name: University of Amsterdam Coordination Redis Settings API
  slug: university-of-amsterdam-coordination-redis-settings-api
- description: The Cost Tracking API from University of Amsterdam — 3 operation(s) for cost tracking.
  name: University of Amsterdam Cost Tracking API
  slug: university-of-amsterdam-cost-tracking-api
- description: The credential management API from University of Amsterdam — 6 operation(s) for credential management.
  name: University of Amsterdam credential management API
  slug: university-of-amsterdam-credential-management-api
- description: The Cursor Pass-through API from University of Amsterdam — 1 operation(s) for cursor pass-through.
  name: University of Amsterdam Cursor Pass-through API
  slug: university-of-amsterdam-cursor-pass-through-api
- description: The Customer Management API from University of Amsterdam — 8 operation(s) for customer management.
  name: University of Amsterdam Customer Management API
  slug: university-of-amsterdam-customer-management-api
- description: The Debug API from University of Amsterdam — 1 operation(s) for debug.
  name: University of Amsterdam Debug API
  slug: university-of-amsterdam-debug-api
- description: The email management API from University of Amsterdam — 2 operation(s) for email management.
  name: University of Amsterdam email management API
  slug: university-of-amsterdam-email-management-api
- description: The embeddings API from University of Amsterdam — 4 operation(s) for embeddings.
  name: University of Amsterdam Embeddings API
  slug: university-of-amsterdam-embeddings-api
- description: The evals API from University of Amsterdam — 5 operation(s) for evals.
  name: University of Amsterdam Evals API
  slug: university-of-amsterdam-evals-api
- description: The experimental API from University of Amsterdam — 1 operation(s) for experimental.
  name: University of Amsterdam Experimental API
  slug: university-of-amsterdam-experimental-api
- description: The Fallback Management API from University of Amsterdam — 2 operation(s) for fallback management.
  name: University of Amsterdam Fallback Management API
  slug: university-of-amsterdam-fallback-management-api
- description: The files API from University of Amsterdam — 9 operation(s) for files.
  name: University of Amsterdam Files API
  slug: university-of-amsterdam-files-api
- description: The fine-tuning API from University of Amsterdam — 6 operation(s) for fine-tuning.
  name: University of Amsterdam Fine Tuning API
  slug: university-of-amsterdam-fine-tuning-api
- description: The gemini_agents API from University of Amsterdam — 1 operation(s) for gemini_agents.
  name: University of Amsterdam Gemini Agents API
  slug: university-of-amsterdam-gemini-agents-api
- description: The Google AI Studio Pass-through API from University of Amsterdam — 1 operation(s) for google ai studio pass-through.
  name: University of Amsterdam Google AI Studio Pass-through API
  slug: university-of-amsterdam-google-ai-studio-pass-through-api
- description: The google genai endpoints API from University of Amsterdam — 12 operation(s) for google genai endpoints.
  name: University of Amsterdam google genai endpoints API
  slug: university-of-amsterdam-google-genai-endpoints-api
- description: The Guardrails API from University of Amsterdam — 20 operation(s) for guardrails.
  name: University of Amsterdam Guardrails API
  slug: university-of-amsterdam-guardrails-api
- description: The health API from University of Amsterdam — 16 operation(s) for health.
  name: University of Amsterdam Health API
  slug: university-of-amsterdam-health-api
- description: The images API from University of Amsterdam — 6 operation(s) for images.
  name: University of Amsterdam Images API
  slug: university-of-amsterdam-images-api
- description: The interactions API from University of Amsterdam — 6 operation(s) for interactions.
  name: University of Amsterdam Interactions API
  slug: university-of-amsterdam-interactions-api
- description: The Internal User management API from University of Amsterdam — 10 operation(s) for internal user management.
  name: University of Amsterdam Internal User management API
  slug: university-of-amsterdam-internal-user-management-api
- description: The jwt_mappings API from University of Amsterdam — 5 operation(s) for jwt_mappings.
  name: University of Amsterdam JWT Mappings API
  slug: university-of-amsterdam-jwt-mappings-api
- description: The key management API from University of Amsterdam — 15 operation(s) for key management.
  name: University of Amsterdam key management API
  slug: university-of-amsterdam-key-management-api
- description: The langfuse_passthrough API from University of Amsterdam — 1 operation(s) for langfuse_passthrough.
  name: University of Amsterdam Langfuse Passthrough API
  slug: university-of-amsterdam-langfuse-passthrough-api
- description: The LiteLLM API API from University of Amsterdam — 1 operation(s) for litellm api.
  name: University of Amsterdam LiteLLM API
  slug: university-of-amsterdam-litellm-api-api
- description: The Litellm API from University of Amsterdam — 1 operation(s) for litellm.
  name: University of Amsterdam Litellm API
  slug: university-of-amsterdam-litellm-api
- description: The llm utils API from University of Amsterdam — 3 operation(s) for llm utils.
  name: University of Amsterdam llm utils API
  slug: university-of-amsterdam-llm-utils-api
- description: The Logging Callbacks API from University of Amsterdam — 2 operation(s) for logging callbacks.
  name: University of Amsterdam Logging Callbacks API
  slug: university-of-amsterdam-logging-callbacks-api
- description: The Mcp API from University of Amsterdam — 28 operation(s) for mcp.
  name: University of Amsterdam MCP API
  slug: university-of-amsterdam-mcp-api
- description: The memory management API from University of Amsterdam — 2 operation(s) for memory management.
  name: University of Amsterdam memory management API
  slug: university-of-amsterdam-memory-management-api
- description: The Milvus Pass-through API from University of Amsterdam — 1 operation(s) for milvus pass-through.
  name: University of Amsterdam Milvus Pass-through API
  slug: university-of-amsterdam-milvus-pass-through-api
- description: The Mistral Pass-through API from University of Amsterdam — 1 operation(s) for mistral pass-through.
  name: University of Amsterdam Mistral Pass-through API
  slug: university-of-amsterdam-mistral-pass-through-api
- description: The model management API from University of Amsterdam — 24 operation(s) for model management.
  name: University of Amsterdam model management API
  slug: university-of-amsterdam-model-management-api
- description: The moderations API from University of Amsterdam — 2 operation(s) for moderations.
  name: University of Amsterdam Moderations API
  slug: university-of-amsterdam-moderations-api
- description: The ocr API from University of Amsterdam — 2 operation(s) for ocr.
  name: University of Amsterdam Ocr API
  slug: university-of-amsterdam-ocr-api
- description: The OpenAI Pass-through API from University of Amsterdam — 2 operation(s) for openai pass-through.
  name: University of Amsterdam OpenAI Pass-through API
  slug: university-of-amsterdam-openai-pass-through-api
- description: The organization management API from University of Amsterdam — 9 operation(s) for organization management.
  name: University of Amsterdam organization management API
  slug: university-of-amsterdam-organization-management-api
- description: The pass-through API from University of Amsterdam — 17 operation(s) for pass-through.
  name: University of Amsterdam Pass Through API
  slug: university-of-amsterdam-pass-through-api
- description: The plugins API from University of Amsterdam — 2 operation(s) for plugins.
  name: University of Amsterdam Plugins API
  slug: university-of-amsterdam-plugins-api
- description: The Policies API from University of Amsterdam — 23 operation(s) for policies.
  name: University of Amsterdam Policies API
  slug: university-of-amsterdam-policies-api
- description: The policy_resolve API from University of Amsterdam — 2 operation(s) for policy_resolve.
  name: University of Amsterdam Policy Resolve API
  slug: university-of-amsterdam-policy-resolve-api
- description: The project management API from University of Amsterdam — 5 operation(s) for project management.
  name: University of Amsterdam project management API
  slug: university-of-amsterdam-project-management-api
- description: The Prompt Management API from University of Amsterdam — 6 operation(s) for prompt management.
  name: University of Amsterdam Prompt Management API
  slug: university-of-amsterdam-prompt-management-api
- description: The prompts API from University of Amsterdam — 1 operation(s) for prompts.
  name: University of Amsterdam Prompts API
  slug: university-of-amsterdam-prompts-api
- description: The Provider API from University of Amsterdam — 1 operation(s) for provider.
  name: University of Amsterdam Provider API
  slug: university-of-amsterdam-provider-api
- description: The providers API from University of Amsterdam — 2 operation(s) for providers.
  name: University of Amsterdam Providers API
  slug: university-of-amsterdam-providers-api
- description: The public API from University of Amsterdam — 11 operation(s) for public.
  name: University of Amsterdam Public API
  slug: university-of-amsterdam-public-api
- description: The rag API from University of Amsterdam — 4 operation(s) for rag.
  name: University of Amsterdam Rag API
  slug: university-of-amsterdam-rag-api
- description: The realtime API from University of Amsterdam — 6 operation(s) for realtime.
  name: University of Amsterdam Realtime API
  slug: university-of-amsterdam-realtime-api
- description: The rerank API from University of Amsterdam — 3 operation(s) for rerank.
  name: University of Amsterdam Rerank API
  slug: university-of-amsterdam-rerank-api
- description: The responses API from University of Amsterdam — 16 operation(s) for responses.
  name: University of Amsterdam Responses API
  slug: university-of-amsterdam-responses-api
- description: The Robots.txt API from University of Amsterdam — 1 operation(s) for robots.txt.
  name: University of Amsterdam Robots.txt API
  slug: university-of-amsterdam-robots-txt-api
- description: The Router Settings API from University of Amsterdam — 2 operation(s) for router settings.
  name: University of Amsterdam Router Settings API
  slug: university-of-amsterdam-router-settings-api
- description: The Routes API from University of Amsterdam — 1 operation(s) for routes.
  name: University of Amsterdam Routes API
  slug: university-of-amsterdam-routes-api
- description: The rust control plane API from University of Amsterdam — 1 operation(s) for rust control plane.
  name: University of Amsterdam rust control plane API
  slug: university-of-amsterdam-rust-control-plane-api
- description: The scim API from University of Amsterdam — 10 operation(s) for scim.
  name: University of Amsterdam SCIM API
  slug: university-of-amsterdam-scim-api
- description: The search API from University of Amsterdam — 6 operation(s) for search.
  name: University of Amsterdam Search API
  slug: university-of-amsterdam-search-api
- description: The search_tools API from University of Amsterdam — 5 operation(s) for search_tools.
  name: University of Amsterdam Search Tools API
  slug: university-of-amsterdam-search-tools-api
- description: The Settings API from University of Amsterdam — 2 operation(s) for settings.
  name: University of Amsterdam Settings API
  slug: university-of-amsterdam-settings-api
- description: The SSO Settings API from University of Amsterdam — 6 operation(s) for sso settings.
  name: University of Amsterdam SSO Settings API
  slug: university-of-amsterdam-sso-settings-api
- description: The tag management API from University of Amsterdam — 12 operation(s) for tag management.
  name: University of Amsterdam tag management API
  slug: university-of-amsterdam-tag-management-api
- description: The Team API from University of Amsterdam — 1 operation(s) for team.
  name: University of Amsterdam Team API
  slug: university-of-amsterdam-team-api
- description: The team management API from University of Amsterdam — 22 operation(s) for team management.
  name: University of Amsterdam team management API
  slug: university-of-amsterdam-team-management-api
- description: The tool management API from University of Amsterdam — 8 operation(s) for tool management.
  name: University of Amsterdam tool management API
  slug: university-of-amsterdam-tool-management-api
- description: The Toolset API from University of Amsterdam — 1 operation(s) for toolset.
  name: University of Amsterdam Toolset API
  slug: university-of-amsterdam-toolset-api
- description: The UI Settings API from University of Amsterdam — 2 operation(s) for ui settings.
  name: University of Amsterdam UI Settings API
  slug: university-of-amsterdam-ui-settings-api
- description: The UI Theme Settings API from University of Amsterdam — 3 operation(s) for ui theme settings.
  name: University of Amsterdam UI Theme Settings API
  slug: university-of-amsterdam-ui-theme-settings-api
- description: The usage_ai API from University of Amsterdam — 1 operation(s) for usage_ai.
  name: University of Amsterdam Usage AI API
  slug: university-of-amsterdam-usage-ai-api
- description: The user agent analytics API from University of Amsterdam — 6 operation(s) for user agent analytics.
  name: University of Amsterdam user agent analytics API
  slug: university-of-amsterdam-user-agent-analytics-api
- description: The utils API from University of Amsterdam — 1 operation(s) for utils.
  name: University of Amsterdam Utils API
  slug: university-of-amsterdam-utils-api
- description: The vector store management API from University of Amsterdam — 6 operation(s) for vector store management.
  name: University of Amsterdam vector store management API
  slug: university-of-amsterdam-vector-store-management-api
- description: The vector_stores API from University of Amsterdam — 13 operation(s) for vector_stores.
  name: University of Amsterdam Vector Stores API
  slug: university-of-amsterdam-vector-stores-api
- description: The Vertex AI Pass-through API from University of Amsterdam — 2 operation(s) for vertex ai pass-through.
  name: University of Amsterdam Vertex AI Pass-through API
  slug: university-of-amsterdam-vertex-ai-pass-through-api
- description: The videos API from University of Amsterdam — 16 operation(s) for videos.
  name: University of Amsterdam Videos API
  slug: university-of-amsterdam-videos-api
- description: The VLLM Pass-through API from University of Amsterdam — 1 operation(s) for vllm pass-through.
  name: University of Amsterdam VLLM Pass-through API
  slug: university-of-amsterdam-vllm-pass-through-api
- description: The Watsonx Pass-through API from University of Amsterdam — 1 operation(s) for watsonx pass-through.
  name: University of Amsterdam Watsonx Pass-through API
  slug: university-of-amsterdam-watsonx-pass-through-api
- description: The WebSocket API from University of Amsterdam — 6 operation(s) for websocket.
  name: University of Amsterdam Web Socket API
  slug: university-of-amsterdam-websocket-api
- description: The .well Known API from University of Amsterdam — 1 operation(s) for .well known.
  name: University of Amsterdam .well Known API
  slug: university-of-amsterdam-well-known-api
- description: The workflow management API from University of Amsterdam — 4 operation(s) for workflow management.
  name: University of Amsterdam workflow management API
  slug: university-of-amsterdam-workflow-management-api
artifact_total: 130
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-amsterdam-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.uva.nl/en
- group: other
  title: ''
  type: OpenData
  url: https://uba.uva.nl/en/support/open-data/open-data.html
- group: other
  title: ''
  type: OpenData
  url: https://uba.uva.nl/en/support/open-data/data-sets-and-publication-channels/data-sets-and-publication-channels.html
- group: docs
  title: ''
  type: Documentation
  url: https://uba.uva.nl/en/support/open-data/licences/licences.html
- group: other
  title: ''
  type: ResearchRepository
  url: https://dare.uva.nl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://uvaauas.figshare.com/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://uba.uva.nl/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://studiegids.uva.nl/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://datanose.nl/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.uva.nl/federationmetadata/2007-06/federationmetadata.xml
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uva.nl/en/about-the-uva/about-the-university/ai/ai.html
- group: build
  title: ''
  type: AITooling
  url: https://github.com/uva/UvA-HvA-Agentic-Tools
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uva
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.uva.nl/.well-known/security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uva.nl/en/home/disclaimers/about-this-site
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uva.nl/en/home/disclaimers/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://www.uva.nl/en/about-the-uva/contact-and-locations/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.uva.nl/en/news-events/news/uva-news.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-amsterdam/
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-amsterdam-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-amsterdam-conformance.yml
- group: design
  title: ''
  type: x-errors
  url: errors/university-of-amsterdam-errors.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/university-of-amsterdam-vocabulary.yml
- group: design
  title: ''
  type: x-json-ld-context
  url: json-ld/university-of-amsterdam-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-amsterdam-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-amsterdam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-amsterdam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-amsterdam-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Amsterdam (Universiteit van Amsterdam, UvA) is a public research university in Amsterdam, Netherlands, a LERU member and one of the two large research universities in the city. It operates no central developer portal and issues no public API keys, and the honest shape of its programmable footprint is three institution-run surfaces surrounded by six vendor platforms it is a tenant of. What it genuinely runs itself: a shared AI gateway with the Amsterdam University of Applied Sciences at llmproxy.uva.nl that serves a full OpenAPI 3.1 description and issues keys to staff, students and developers on request; a SAML 2.0 identity provider whose signed federation metadata is published on its own host and registered in SURFconext and eduGAIN; and the DataNose course and registration API on its own network, whose Swagger UI answers but whose generated description currently returns 500. Everything else that looks like a UvA API is a contract someone else wrote: the
  library''s Linked Open Data platform is a TriplyDB tenancy, the research repository is Figshare, UvA-DARE and its OAI-PMH feed are Elsevier Pure, the archives OAI provider is LYRASIS-hosted ArchivesSpace, the central catalogue OAI endpoint is Ex Libris Alma and now returns 403 to the public, and the timetable API is Eveoh MyTimetable behind SSO. The data in those systems is the university''s; the interfaces are not.'
examples:
- key_count: 20
  name: University Of Amsterdam Get Dataset Example
  slug: university-of-amsterdam-get-dataset-example
- key_count: 2
  name: University Of Amsterdam Sparql Query Example
  slug: university-of-amsterdam-sparql-query-example
finops:
- name: University Of Amsterdam Finops
  service_category: Education
  slug: university-of-amsterdam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-amsterdam.png
jsonld:
- class_count: 15
  name: University Of Amsterdam Context
  property_count: 14
  slug: university-of-amsterdam-context
layout: provider
modified: '2026-08-19'
name: University of Amsterdam
nav: Providers
network: true
overview: 'University of Amsterdam publishes 114 APIs on the [APIs.io](https://apis.io/) network, including A2a API, A2a Registration API, access group management API, and 111 more. Tagged areas include University, Higher Education, Education, Public Research University, and Netherlands.


  The University of Amsterdam catalog on APIs.io includes 1 JSON-LD context.


  University of Amsterdam''s developer surface includes documentation, support, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: University Of Amsterdam Plans Pricing
  plan_count: 2
  slug: university-of-amsterdam-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: University Of Amsterdam Rate Limits
  slug: university-of-amsterdam-rate-limits
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 61.0
    developer_ergonomics: 35.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 44.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-amsterdam/refs/heads/main/screenshots/university-of-amsterdam-2026-08-17T083414.png
security:
- kind: authentication
  name: University Of Amsterdam Authentication
  slug: university-of-amsterdam-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: University Of Amsterdam Domain Security
  slug: university-of-amsterdam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-amsterdam
tags:
- University
- Higher Education
- Education
- Public Research University
- Netherlands
- Europe
- LERU
- Open Data
- Linked Data
- Library
- Research Data
- Research Repository
- Course Catalog
- Identity Federation
- OAI-PMH
- Artificial Intelligence
website: https://www.uva.nl/en
---
