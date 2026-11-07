---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: half
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 357
  human_in_the_loop: 4
  name: Piknik Spot Agentic Access
  operation_count: 683
  slug: piknik-spot-agentic-access
  summary_line: 683 operations · 357 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: Hosted, remote Model Context Protocol server (protocol 2025-03-26, Streamable HTTP with an SSE endpoint at /api/mcp/sse) exposing 62 tools and 7 piknik:// resources for local-food discovery, Local Foo
  name: Piknik.Spot MCP Server
  slug: piknikspot-mcp-server
- description: 'Agent-to-Agent (A2A 1.0) agent served from the provider''s own host: the agent card at /.well-known/agent-card.json (also at the legacy /.well-known/agent.json, byte-identical) declares five public ski'
  name: Piknik.Spot A2A Agent
  slug: piknikspot-a2a-agent
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The A2A Agents API from Piknik.Spot — 43 operation(s) for a2a agents.
  name: Piknik.Spot A2A Agents API
  slug: piknik-spot-a2a-agents-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The A2a API from Piknik.Spot — 1 operation(s) for a2a.
  name: Piknik.Spot A2a API
  slug: piknik-spot-a2a-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Admin API from Piknik.Spot — 91 operation(s) for admin.
  name: Piknik.Spot Admin API
  slug: piknik-spot-admin-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Agritourism API from Piknik.Spot — 37 operation(s) for agritourism.
  name: Piknik.Spot Agritourism API
  slug: piknik-spot-agritourism-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The AI Agents API from Piknik.Spot — 6 operation(s) for ai agents.
  name: Piknik.Spot AI Agents API
  slug: piknik-spot-ai-agents-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Analytics API from Piknik.Spot — 6 operation(s) for analytics.
  name: Piknik.Spot Analytics API
  slug: piknik-spot-analytics-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Associations API from Piknik.Spot — 19 operation(s) for associations.
  name: Piknik.Spot Associations API
  slug: piknik-spot-associations-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Authentication API from Piknik.Spot — 5 operation(s) for authentication.
  name: Piknik.Spot Authentication API
  slug: piknik-spot-authentication-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Baskets API from Piknik.Spot — 2 operation(s) for baskets.
  name: Piknik.Spot Baskets API
  slug: piknik-spot-baskets-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Browse Products API from Piknik.Spot — 1 operation(s) for browse products.
  name: Piknik.Spot Browse Products API
  slug: piknik-spot-browse-products-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Business API from Piknik.Spot — 4 operation(s) for business.
  name: Piknik.Spot Business API
  slug: piknik-spot-business-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Categories API from Piknik.Spot — 1 operation(s) for categories.
  name: Piknik.Spot Categories API
  slug: piknik-spot-categories-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Community API from Piknik.Spot — 2 operation(s) for community.
  name: Piknik.Spot Community API
  slug: piknik-spot-community-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Community Food Score Pdf API from Piknik.Spot — 1 operation(s) for community food score pdf.
  name: Piknik.Spot Community Food Score Pdf API
  slug: piknik-spot-community-food-score-pdf-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Config API from Piknik.Spot — 1 operation(s) for config.
  name: Piknik.Spot Config API
  slug: piknik-spot-config-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Connections API from Piknik.Spot — 3 operation(s) for connections.
  name: Piknik.Spot Connections API
  slug: piknik-spot-connections-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Contact API from Piknik.Spot — 1 operation(s) for contact.
  name: Piknik.Spot Contact API
  slug: piknik-spot-contact-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Cron API from Piknik.Spot — 1 operation(s) for cron.
  name: Piknik.Spot Cron API
  slug: piknik-spot-cron-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The CSA API from Piknik.Spot — 9 operation(s) for csa.
  name: Piknik.Spot CSA API
  slug: piknik-spot-csa-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Cuisines API from Piknik.Spot — 1 operation(s) for cuisines.
  name: Piknik.Spot Cuisines API
  slug: piknik-spot-cuisines-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Debug API from Piknik.Spot — 1 operation(s) for debug.
  name: Piknik.Spot Debug API
  slug: piknik-spot-debug-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Dev API from Piknik.Spot — 3 operation(s) for dev.
  name: Piknik.Spot Dev API
  slug: piknik-spot-dev-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Discussions API from Piknik.Spot — 7 operation(s) for discussions.
  name: Piknik.Spot Discussions API
  slug: piknik-spot-discussions-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Endorsements API from Piknik.Spot — 2 operation(s) for endorsements.
  name: Piknik.Spot Endorsements API
  slug: piknik-spot-endorsements-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Engagement Metrics API from Piknik.Spot — 1 operation(s) for engagement metrics.
  name: Piknik.Spot Engagement Metrics API
  slug: piknik-spot-engagement-metrics-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Events API from Piknik.Spot — 25 operation(s) for events.
  name: Piknik.Spot Events API
  slug: piknik-spot-events-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Feature Flags API from Piknik.Spot — 1 operation(s) for feature flags.
  name: Piknik.Spot Feature Flags API
  slug: piknik-spot-feature-flags-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Feedback API from Piknik.Spot — 1 operation(s) for feedback.
  name: Piknik.Spot Feedback API
  slug: piknik-spot-feedback-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Follow API from Piknik.Spot — 1 operation(s) for follow.
  name: Piknik.Spot Follow API
  slug: piknik-spot-follow-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Followed Announcements API from Piknik.Spot — 1 operation(s) for followed announcements.
  name: Piknik.Spot Followed Announcements API
  slug: piknik-spot-followed-announcements-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Following API from Piknik.Spot — 1 operation(s) for following.
  name: Piknik.Spot Following API
  slug: piknik-spot-following-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Food Score API from Piknik.Spot — 1 operation(s) for food score.
  name: Piknik.Spot Food Score API
  slug: piknik-spot-food-score-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The For Real Estate API from Piknik.Spot — 2 operation(s) for for real estate.
  name: Piknik.Spot For Real Estate API
  slug: piknik-spot-for-real-estate-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Games API from Piknik.Spot — 11 operation(s) for games.
  name: Piknik.Spot Games API
  slug: piknik-spot-games-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Geocode API from Piknik.Spot — 2 operation(s) for geocode.
  name: Piknik.Spot Geocode API
  slug: piknik-spot-geocode-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Global Features API from Piknik.Spot — 1 operation(s) for global features.
  name: Piknik.Spot Global Features API
  slug: piknik-spot-global-features-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Invitations API from Piknik.Spot — 2 operation(s) for invitations.
  name: Piknik.Spot Invitations API
  slug: piknik-spot-invitations-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Jobs API from Piknik.Spot — 5 operation(s) for jobs.
  name: Piknik.Spot Jobs API
  slug: piknik-spot-jobs-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Local Food Score API from Piknik.Spot — 3 operation(s) for local food score.
  name: Piknik.Spot Local Food Score API
  slug: piknik-spot-local-food-score-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Local Food Score Narrative Pdf API from Piknik.Spot — 1 operation(s) for local food score narrative pdf.
  name: Piknik.Spot Local Food Score Narrative Pdf API
  slug: piknik-spot-local-food-score-narrative-pdf-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Local Food Score Pdf API from Piknik.Spot — 1 operation(s) for local food score pdf.
  name: Piknik.Spot Local Food Score Pdf API
  slug: piknik-spot-local-food-score-pdf-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Marketplace API from Piknik.Spot — 15 operation(s) for marketplace.
  name: Piknik.Spot Marketplace API
  slug: piknik-spot-marketplace-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The MCP API from Piknik.Spot — 6 operation(s) for mcp.
  name: Piknik.Spot MCP API
  slug: piknik-spot-mcp-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Me API from Piknik.Spot — 1 operation(s) for me.
  name: Piknik.Spot Me API
  slug: piknik-spot-me-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Metadata API from Piknik.Spot — 1 operation(s) for metadata.
  name: Piknik.Spot Metadata API
  slug: piknik-spot-metadata-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The My Businesses API from Piknik.Spot — 1 operation(s) for my businesses.
  name: Piknik.Spot My Businesses API
  slug: piknik-spot-my-businesses-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Notifications API from Piknik.Spot — 8 operation(s) for notifications.
  name: Piknik.Spot Notifications API
  slug: piknik-spot-notifications-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The OAuth API from Piknik.Spot — 9 operation(s) for oauth.
  name: Piknik.Spot OAuth API
  slug: piknik-spot-oauth-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Offerings API from Piknik.Spot — 1 operation(s) for offerings.
  name: Piknik.Spot Offerings API
  slug: piknik-spot-offerings-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Ontario Food Score Heatmap API from Piknik.Spot — 1 operation(s) for ontario food score heatmap.
  name: Piknik.Spot Ontario Food Score Heatmap API
  slug: piknik-spot-ontario-food-score-heatmap-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Participants API from Piknik.Spot — 49 operation(s) for participants.
  name: Piknik.Spot Participants API
  slug: piknik-spot-participants-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Piknik Durham Report Card Pdf API from Piknik.Spot — 1 operation(s) for piknik durham report card pdf.
  name: Piknik.Spot Piknik Durham Report Card Pdf API
  slug: piknik-spot-piknik-durham-report-card-pdf-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Piknik.Spot API API from Piknik.Spot — 1 operation(s) for piknik.spot api.
  name: Piknik.Spot Piknik.Spot API
  slug: piknik-spot-piknik-spot-api-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Place API from Piknik.Spot — 11 operation(s) for place.
  name: Piknik.Spot Place API
  slug: piknik-spot-place-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Place Tours API from Piknik.Spot — 4 operation(s) for place tours.
  name: Piknik.Spot Place Tours API
  slug: piknik-spot-place-tours-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Planting Calendar API from Piknik.Spot — 1 operation(s) for planting calendar.
  name: Piknik.Spot Planting Calendar API
  slug: piknik-spot-planting-calendar-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Planting Calendar.ics API from Piknik.Spot — 1 operation(s) for planting calendar.ics.
  name: Piknik.Spot Planting Calendar.ics API
  slug: piknik-spot-planting-calendar-ics-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Products API from Piknik.Spot — 3 operation(s) for products.
  name: Piknik.Spot Products API
  slug: piknik-spot-products-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Profile API from Piknik.Spot — 7 operation(s) for profile.
  name: Piknik.Spot Profile API
  slug: piknik-spot-profile-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Recipes API from Piknik.Spot — 5 operation(s) for recipes.
  name: Piknik.Spot Recipes API
  slug: piknik-spot-recipes-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Recommendations API from Piknik.Spot — 1 operation(s) for recommendations.
  name: Piknik.Spot Recommendations API
  slug: piknik-spot-recommendations-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Regional Score API from Piknik.Spot — 2 operation(s) for regional score.
  name: Piknik.Spot Regional Score API
  slug: piknik-spot-regional-score-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Resiliency API from Piknik.Spot — 1 operation(s) for resiliency.
  name: Piknik.Spot Resiliency API
  slug: piknik-spot-resiliency-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Scan API from Piknik.Spot — 2 operation(s) for scan.
  name: Piknik.Spot Scan API
  slug: piknik-spot-scan-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Search API from Piknik.Spot — 1 operation(s) for search.
  name: Piknik.Spot Search API
  slug: piknik-spot-search-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Seasonal Guide API from Piknik.Spot — 1 operation(s) for seasonal guide.
  name: Piknik.Spot Seasonal Guide API
  slug: piknik-spot-seasonal-guide-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Service Locations API from Piknik.Spot — 1 operation(s) for service locations.
  name: Piknik.Spot Service Locations API
  slug: piknik-spot-service-locations-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Skills API from Piknik.Spot — 1 operation(s) for skills.
  name: Piknik.Spot Skills API
  slug: piknik-spot-skills-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Sms API from Piknik.Spot — 1 operation(s) for sms.
  name: Piknik.Spot Sms API
  slug: piknik-spot-sms-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Spend Challenge API from Piknik.Spot — 8 operation(s) for spend challenge.
  name: Piknik.Spot Spend Challenge API
  slug: piknik-spot-spend-challenge-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Sponsor API from Piknik.Spot — 1 operation(s) for sponsor.
  name: Piknik.Spot Sponsor API
  slug: piknik-spot-sponsor-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Sponsorships API from Piknik.Spot — 1 operation(s) for sponsorships.
  name: Piknik.Spot Sponsorships API
  slug: piknik-spot-sponsorships-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Surveys API from Piknik.Spot — 7 operation(s) for surveys.
  name: Piknik.Spot Surveys API
  slug: piknik-spot-surveys-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Tasks API from Piknik.Spot — 16 operation(s) for tasks.
  name: Piknik.Spot Tasks API
  slug: piknik-spot-tasks-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Telegram API from Piknik.Spot — 2 operation(s) for telegram.
  name: Piknik.Spot Telegram API
  slug: piknik-spot-telegram-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Test API from Piknik.Spot — 1 operation(s) for test.
  name: Piknik.Spot Test API
  slug: piknik-spot-test-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Thumbs API from Piknik.Spot — 1 operation(s) for thumbs.
  name: Piknik.Spot Thumbs API
  slug: piknik-spot-thumbs-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Upload API from Piknik.Spot — 4 operation(s) for upload.
  name: Piknik.Spot Upload API
  slug: piknik-spot-upload-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Upload Image API from Piknik.Spot — 1 operation(s) for upload image.
  name: Piknik.Spot Upload Image API
  slug: piknik-spot-upload-image-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The User API from Piknik.Spot — 6 operation(s) for user.
  name: Piknik.Spot User API
  slug: piknik-spot-user-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Users API from Piknik.Spot — 8 operation(s) for users.
  name: Piknik.Spot Users API
  slug: piknik-spot-users-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Validation API from Piknik.Spot — 1 operation(s) for validation.
  name: Piknik.Spot Validation API
  slug: piknik-spot-validation-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Visit API from Piknik.Spot — 1 operation(s) for visit.
  name: Piknik.Spot Visit API
  slug: piknik-spot-visit-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Voice API from Piknik.Spot — 2 operation(s) for voice.
  name: Piknik.Spot Voice API
  slug: piknik-spot-voice-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Webhooks API from Piknik.Spot — 5 operation(s) for webhooks.
  name: Piknik.Spot Webhooks API
  slug: piknik-spot-webhooks-api
- baseURL: https://piknik.spot/api
  baseurl_source: declared
  description: The Widget API from Piknik.Spot — 3 operation(s) for widget.
  name: Piknik.Spot Widget API
  slug: piknik-spot-widget-api
- baseURL: https://piknik.spot/api/mcp
  baseurl_source: declared
  description: The Open API API from Piknik.Spot — 2 operation(s) for open api.
  name: Piknik.Spot Open API
  slug: piknik-spot-open-api-api
artifact_total: 102
asyncapis:
- description: ''
  name: Piknik Spot Webhooks
  slug: piknik-spot-webhooks
common:
- group: other
  href: https://artifacts.apis.io/piknik-spot/capabilities/piknik-spot-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/piknik-spot-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://piknik.spot/
- group: auth
  href: https://artifacts.apis.io/piknik-spot/security/piknik-spot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/piknik-spot-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/piknik-spot/agentic-access/piknik-spot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/piknik-spot-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/piknik-spot/scopes/piknik-spot-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/piknik-spot-scopes.yml
- group: auth
  href: https://artifacts.apis.io/piknik-spot/authentication/piknik-spot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/piknik-spot-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://piknik.spot/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://piknik.spot/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://piknik.spot/skills/piknik-rest-api/SKILL.md
- group: operate
  title: ''
  type: Support
  url: https://piknik.spot/contact
- group: start
  title: ''
  type: SignUp
  url: https://piknik.spot/signup
- group: start
  title: ''
  type: Login
  url: https://piknik.spot/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://piknik.spot/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://piknik.spot/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://piknik.spot/llms.txt
- group: agent
  href: https://artifacts.apis.io/piknik-spot/mcp/piknik-spot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/piknik-spot-mcp.yml
- group: other
  href: https://artifacts.apis.io/piknik-spot/a2a/piknik-spot-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/piknik-spot-a2a.yml
- group: agent
  href: https://artifacts.apis.io/piknik-spot/llms/piknik-spot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/piknik-spot-llms.txt
- group: agent
  href: https://artifacts.apis.io/piknik-spot/well-known/piknik-spot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/piknik-spot-well-known.yml
- group: build
  href: https://artifacts.apis.io/piknik-spot/mcp/piknik-spot-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/piknik-spot-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/piknik-spot/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/piknik-spot/conventions/piknik-spot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/piknik-spot-conventions.yml
- group: design
  href: https://artifacts.apis.io/piknik-spot/conventions/piknik-spot-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/piknik-spot-conventions.yml
- group: design
  href: https://artifacts.apis.io/piknik-spot/errors/piknik-spot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/piknik-spot-problem-types.yml
- group: design
  href: https://artifacts.apis.io/piknik-spot/data-model/piknik-spot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/piknik-spot-data-model.yml
- group: operate
  href: https://artifacts.apis.io/piknik-spot/rate-limits/piknik-spot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/piknik-spot-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/piknik-spot/plans/piknik-spot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/piknik-spot-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/piknik-spot/lifecycle/piknik-spot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/piknik-spot-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/piknik-spot/conformance/piknik-spot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/piknik-spot-conformance.yml
- group: other
  href: https://artifacts.apis.io/piknik-spot/overlays/piknik-spot-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/piknik-spot-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/piknik-spot/asyncapi/piknik-spot-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/piknik-spot-webhooks.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://piknik.spot/privacy-policy
created: '2026-09-19'
description: 'Piknik (piknik.spot) is a local food system platform based in Waterloo Region, Ontario, Canada that maps farms, processors, markets, shops, restaurants, community gardens and food hubs, the supply links between them, marketplace listings, community events, jobs and volunteer posts, recipes, and a Local Food Score for any address. It is built agent-first: a REST API under https://piknik.spot/api described by a 683-operation OpenAPI 3.0.3 document, a hosted Model Context Protocol server at https://piknik.spot/api/mcp exposing 62 tools (public discovery tools anonymously, write tools behind OAuth 2.0 with PKCE and dynamic client registration or pik_pat_ personal access tokens), an A2A 1.0 agent card served at /.well-known/agent-card.json with a JSON-RPC endpoint at /api/a2a, an llms.txt, provider-published Agent Skills, and a published Agent Ethics policy that permits only immediate-use access and forbids bulk extraction, retention and model training.'
finops:
- has_sources: true
  method: derived
  name: Piknik Spot Finops
  primary_unit: ''
  service_category: ''
  slug: piknik-spot-finops
  template: true
image: https://piknik.spot/icons/icon-512x512.png
layout: provider
mcp_servers:
- description: Remote MCP server at piknik.spot over HTTP requiring OAuth; 62 tools listed.
  name: Piknik.Spot MCP Server
  slug: piknik
modified: '2026-09-19'
name: Piknik.Spot
nav: Providers
network: true
overview: 'Piknik.Spot publishes 89 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2A Agents API, A2a API, Admin API, and 86 more. Tagged areas include Local Food, Agriculture, Farmers Markets, Marketplace, and Event.


  The Piknik.Spot catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Piknik.Spot''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, and 26 more developer resources.'
plans:
- name: Piknik Spot Plans Pricing
  plan_count: 0
  slug: piknik-spot-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Piknik Spot Rate Limits
  slug: piknik-spot-rate-limits
rules:
- authorship: generated
  effective_rule_count: 114
  extends:
  - spectral:oas
  name: Piknik.Spot API Rules
  rule_count: 73
  severity_counts:
    error: 60
    hint: 0
    info: 3
    warn: 10
  slug: piknik-spot-rules
scopes:
- name: Piknik Spot Scopes
  scope_count: 4
  slug: piknik-spot-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 17.1
    contract_governance: 31.8
    contract_quality: 60.8
    developer_ergonomics: 30.4
    discoverability: 75.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 87
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/piknik-spot/piknik-spot-2026-10-11T112548.png
security:
- kind: authentication
  name: Piknik Spot Authentication
  slug: piknik-spot-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Piknik Spot Domain Security
  slug: piknik-spot-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: piknik-spot-find-local-food-nearby
  slug: piknik-spot-find-local-food-nearby
- name: piknik-spot-post-a-marketplace-listing
  slug: piknik-spot-post-a-marketplace-listing
- name: piknik-spot-publish-a-community-event
  slug: piknik-spot-publish-a-community-event
slug: piknik-spot
tags:
- Local Food
- Agriculture
- Farmers Markets
- Marketplace
- Event
- Job
- Recipes
- Geolocation
- Community
- Food Systems
- MCP
- A2A
- Agent-Native
- Ontario
- Canada
website: https://piknik.spot/
---
