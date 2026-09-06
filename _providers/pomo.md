---
access_model:
  confidence: high
  label: Paid self-serve subscription with a 7-day trial; API access requires an account
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://api.usepomo.ai/api/payment/subscription/plans
  - https://usepomo.ai/llms.txt
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.1
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The ab-groups API from Pomo — 6 operation(s) for ab-groups.
  name: Pomo Ab Groups API
  slug: pomo-ab-groups-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The agent-jobs API from Pomo — 5 operation(s) for agent-jobs.
  name: Pomo Agent Jobs API
  slug: pomo-agent-jobs-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The agentic-chat API from Pomo — 3 operation(s) for agentic-chat.
  name: Pomo Agentic Chat API
  slug: pomo-agentic-chat-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The agentic-conversations API from Pomo — 7 operation(s) for agentic-conversations.
  name: Pomo Agentic Conversations API
  slug: pomo-agentic-conversations-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The agentic-tasks API from Pomo — 5 operation(s) for agentic-tasks.
  name: Pomo Agentic Tasks API
  slug: pomo-agentic-tasks-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The agentic-teams API from Pomo — 49 operation(s) for agentic-teams.
  name: Pomo Agentic Teams API
  slug: pomo-agentic-teams-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The agentic-user API from Pomo — 1 operation(s) for agentic-user.
  name: Pomo Agentic User API
  slug: pomo-agentic-user-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The ai-campaign API from Pomo — 2 operation(s) for ai-campaign.
  name: Pomo AI Campaign API
  slug: pomo-ai-campaign-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The ai-personas API from Pomo — 5 operation(s) for ai-personas.
  name: Pomo AI Personas API
  slug: pomo-ai-personas-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The ai-policy API from Pomo — 9 operation(s) for ai-policy.
  name: Pomo AI Policy API
  slug: pomo-ai-policy-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The ai-product-lab API from Pomo — 9 operation(s) for ai-product-lab.
  name: Pomo AI Product Lab API
  slug: pomo-ai-product-lab-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The ai-testing API from Pomo — 15 operation(s) for ai-testing.
  name: Pomo AI Testing API
  slug: pomo-ai-testing-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The analytics API from Pomo — 2 operation(s) for analytics.
  name: Pomo Analytics API
  slug: pomo-analytics-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The auth API from Pomo — 12 operation(s) for auth.
  name: Pomo Auth API
  slug: pomo-auth-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The brand-workflow API from Pomo — 29 operation(s) for brand-workflow.
  name: Pomo Brand Workflow API
  slug: pomo-brand-workflow-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The brand-workflow-sse API from Pomo — 5 operation(s) for brand-workflow-sse.
  name: Pomo Brand Workflow Sse API
  slug: pomo-brand-workflow-sse-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Budget Estimate API from Pomo — 1 operation(s) for budget estimate.
  name: Pomo Budget Estimate API
  slug: pomo-budget-estimate-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The campaign-analytics API from Pomo — 4 operation(s) for campaign-analytics.
  name: Pomo Campaign Analytics API
  slug: pomo-campaign-analytics-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Campaign Geo API from Pomo — 2 operation(s) for campaign geo.
  name: Pomo Campaign Geo API
  slug: pomo-campaign-geo-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The campaign-ideas API from Pomo — 2 operation(s) for campaign-ideas.
  name: Pomo Campaign Ideas API
  slug: pomo-campaign-ideas-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Campaign Images API from Pomo — 5 operation(s) for campaign images.
  name: Pomo Campaign Images API
  slug: pomo-campaign-images-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The campaigns API from Pomo — 116 operation(s) for campaigns.
  name: Pomo Campaigns API
  slug: pomo-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The change-management API from Pomo — 10 operation(s) for change-management.
  name: Pomo Change Management API
  slug: pomo-change-management-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The chat API from Pomo — 5 operation(s) for chat.
  name: Pomo Chat API
  slug: pomo-chat-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The company-profile-access API from Pomo — 3 operation(s) for company-profile-access.
  name: Pomo Company Profile Access API
  slug: pomo-company-profile-access-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The company-profile API from Pomo — 17 operation(s) for company-profile.
  name: Pomo Company Profile API
  slug: pomo-company-profile-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The competitive-gap-analysis API from Pomo — 8 operation(s) for competitive-gap-analysis.
  name: Pomo Competitive Gap Analysis API
  slug: pomo-competitive-gap-analysis-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The competitor-ad-insights API from Pomo — 3 operation(s) for competitor-ad-insights.
  name: Pomo Competitor Ad Insights API
  slug: pomo-competitor-ad-insights-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The competitor-tracking API from Pomo — 23 operation(s) for competitor-tracking.
  name: Pomo Competitor Tracking API
  slug: pomo-competitor-tracking-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The consumer-group API from Pomo — 6 operation(s) for consumer-group.
  name: Pomo Consumer Group API
  slug: pomo-consumer-group-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The contact-submissions API from Pomo — 2 operation(s) for contact-submissions.
  name: Pomo Contact Submissions API
  slug: pomo-contact-submissions-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The content-editing API from Pomo — 3 operation(s) for content-editing.
  name: Pomo Content Editing API
  slug: pomo-content-editing-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The credits API from Pomo — 7 operation(s) for credits.
  name: Pomo Credits API
  slug: pomo-credits-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The crm API from Pomo — 5 operation(s) for crm.
  name: Pomo CRM API
  slug: pomo-crm-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The crm-b2b-leads API from Pomo — 7 operation(s) for crm-b2b-leads.
  name: Pomo CRM B2b Leads API
  slug: pomo-crm-b2b-leads-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The crm-people API from Pomo — 6 operation(s) for crm-people.
  name: Pomo CRM People API
  slug: pomo-crm-people-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Dayparting API from Pomo — 6 operation(s) for dayparting.
  name: Pomo Dayparting API
  slug: pomo-dayparting-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The debug API from Pomo — 1 operation(s) for debug.
  name: Pomo Debug API
  slug: pomo-debug-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The document-jobs API from Pomo — 4 operation(s) for document-jobs.
  name: Pomo Document Jobs API
  slug: pomo-document-jobs-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The earned-media API from Pomo — 17 operation(s) for earned-media.
  name: Pomo Earned Media API
  slug: pomo-earned-media-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Email Campaigns API from Pomo — 14 operation(s) for email campaigns.
  name: Pomo Email Campaigns API
  slug: pomo-email-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Email Campaigns V2 API from Pomo — 8 operation(s) for email campaigns v2.
  name: Pomo Email Campaigns V2 API
  slug: pomo-email-campaigns-v2-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The experiment-packages API from Pomo — 5 operation(s) for experiment-packages.
  name: Pomo Experiment Packages API
  slug: pomo-experiment-packages-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The external-platform API from Pomo — 175 operation(s) for external-platform.
  name: Pomo External Platform API
  slug: pomo-external-platform-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The feedback API from Pomo — 4 operation(s) for feedback.
  name: Pomo Feedback API
  slug: pomo-feedback-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The feeling-lucky API from Pomo — 1 operation(s) for feeling-lucky.
  name: Pomo Feeling Lucky API
  slug: pomo-feeling-lucky-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The first-party-data API from Pomo — 9 operation(s) for first-party-data.
  name: Pomo First Party Data API
  slug: pomo-first-party-data-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The gallery API from Pomo — 12 operation(s) for gallery.
  name: Pomo Gallery API
  slug: pomo-gallery-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The gallery-media API from Pomo — 1 operation(s) for gallery-media.
  name: Pomo Gallery Media API
  slug: pomo-gallery-media-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The google_display_campaigns API from Pomo — 6 operation(s) for google_display_campaigns.
  name: Pomo Google Display Campaigns API
  slug: pomo-google-display-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The google_search_campaigns API from Pomo — 4 operation(s) for google_search_campaigns.
  name: Pomo Google Search Campaigns API
  slug: pomo-google-search-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Google Video Ads API from Pomo — 6 operation(s) for google video ads.
  name: Pomo Google Video Ads API
  slug: pomo-google-video-ads-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The GPT Backend API API from Pomo — 1 operation(s) for gpt backend api.
  name: Pomo GPT Backend API
  slug: pomo-gpt-backend-api-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The guided-workflow API from Pomo — 10 operation(s) for guided-workflow.
  name: Pomo Guided Workflow API
  slug: pomo-guided-workflow-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Health API from Pomo — 8 operation(s) for health.
  name: Pomo Health API
  slug: pomo-health-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The image-operations API from Pomo — 2 operation(s) for image-operations.
  name: Pomo Image Operations API
  slug: pomo-image-operations-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The images API from Pomo — 2 operation(s) for images.
  name: Pomo Images API
  slug: pomo-images-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The influencer-campaigns API from Pomo — 14 operation(s) for influencer-campaigns.
  name: Pomo Influencer Campaigns API
  slug: pomo-influencer-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The influencer-discovery API from Pomo — 35 operation(s) for influencer-discovery.
  name: Pomo Influencer Discovery API
  slug: pomo-influencer-discovery-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The influencer-inventory API from Pomo — 8 operation(s) for influencer-inventory.
  name: Pomo Influencer Inventory API
  slug: pomo-influencer-inventory-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The legal API from Pomo — 1 operation(s) for legal.
  name: Pomo Legal API
  slug: pomo-legal-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The limits API from Pomo — 1 operation(s) for limits.
  name: Pomo Limits API
  slug: pomo-limits-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The linkedin_image_campaigns API from Pomo — 4 operation(s) for linkedin_image_campaigns.
  name: Pomo Linkedin Image Campaigns API
  slug: pomo-linkedin-image-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The linkedin_video_campaigns API from Pomo — 4 operation(s) for linkedin_video_campaigns.
  name: Pomo Linkedin Video Campaigns API
  slug: pomo-linkedin-video-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Llms.txt API from Pomo — 1 operation(s) for llms.txt.
  name: Pomo Llms.txt API
  slug: pomo-llms-txt-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The market-intelligence API from Pomo — 27 operation(s) for market-intelligence.
  name: Pomo Market Intelligence API
  slug: pomo-market-intelligence-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The marketing-docs API from Pomo — 5 operation(s) for marketing-docs.
  name: Pomo Marketing Docs API
  slug: pomo-marketing-docs-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The marketing-wizard API from Pomo — 5 operation(s) for marketing-wizard.
  name: Pomo Marketing Wizard API
  slug: pomo-marketing-wizard-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The mcp API from Pomo — 7 operation(s) for mcp.
  name: Pomo MCP API
  slug: pomo-mcp-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The meta_feed_campaigns API from Pomo — 7 operation(s) for meta_feed_campaigns.
  name: Pomo Meta Feed Campaigns API
  slug: pomo-meta-feed-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The meta_stories_reels_campaigns API from Pomo — 5 operation(s) for meta_stories_reels_campaigns.
  name: Pomo Meta Stories Reels Campaigns API
  slug: pomo-meta-stories-reels-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The metrics API from Pomo — 1 operation(s) for metrics.
  name: Pomo Metrics API
  slug: pomo-metrics-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The notifications API from Pomo — 7 operation(s) for notifications.
  name: Pomo Notifications API
  slug: pomo-notifications-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Online Ad Campaigns API from Pomo — 53 operation(s) for online ad campaigns.
  name: Pomo Online Ad Campaigns API
  slug: pomo-online-ad-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The organization API from Pomo — 19 operation(s) for organization.
  name: Pomo Organization API
  slug: pomo-organization-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The overview API from Pomo — 1 operation(s) for overview.
  name: Pomo Overview API
  slug: pomo-overview-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The payment API from Pomo — 21 operation(s) for payment.
  name: Pomo Payment API
  slug: pomo-payment-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The pricing API from Pomo — 1 operation(s) for pricing.
  name: Pomo Pricing API
  slug: pomo-pricing-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Product Brainstorm API from Pomo — 4 operation(s) for product brainstorm.
  name: Pomo Product Brainstorm API
  slug: pomo-product-brainstorm-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Product Brainstorm Test API from Pomo — 5 operation(s) for product brainstorm test.
  name: Pomo Product Brainstorm Test API
  slug: pomo-product-brainstorm-test-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The product-offerings API from Pomo — 21 operation(s) for product-offerings.
  name: Pomo Product Offerings API
  slug: pomo-product-offerings-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The profile-content-editor API from Pomo — 3 operation(s) for profile-content-editor.
  name: Pomo Profile Content Editor API
  slug: pomo-profile-content-editor-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The programmatic API from Pomo — 3 operation(s) for programmatic.
  name: Pomo Programmatic API
  slug: pomo-programmatic-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The programmatic-keys API from Pomo — 3 operation(s) for programmatic-keys.
  name: Pomo Programmatic Keys API
  slug: pomo-programmatic-keys-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The quickbooks API from Pomo — 7 operation(s) for quickbooks.
  name: Pomo Quickbooks API
  slug: pomo-quickbooks-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Robots.txt API from Pomo — 1 operation(s) for robots.txt.
  name: Pomo Robots.txt API
  slug: pomo-robots-txt-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The SEO Analysis API from Pomo — 14 operation(s) for seo analysis.
  name: Pomo SEO Analysis API
  slug: pomo-seo-analysis-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Sitemap.xml API from Pomo — 1 operation(s) for sitemap.xml.
  name: Pomo Sitemap.xml API
  slug: pomo-sitemap-xml-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The social-platform API from Pomo — 4 operation(s) for social-platform.
  name: Pomo Social Platform API
  slug: pomo-social-platform-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Social Post Campaigns API from Pomo — 21 operation(s) for social post campaigns.
  name: Pomo Social Post Campaigns API
  slug: pomo-social-post-campaigns-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The social-posts API from Pomo — 7 operation(s) for social-posts.
  name: Pomo Social Posts API
  slug: pomo-social-posts-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Test Logging API from Pomo — 1 operation(s) for test logging.
  name: Pomo Test Logging API
  slug: pomo-test-logging-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The TikTok Video Ads API from Pomo — 6 operation(s) for tiktok video ads.
  name: Pomo TikTok Video Ads API
  slug: pomo-tiktok-video-ads-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The udm API from Pomo — 45 operation(s) for udm.
  name: Pomo Udm API
  slug: pomo-udm-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The Unified Data Model API from Pomo — 45 operation(s) for unified data model.
  name: Pomo Unified Data Model API
  slug: pomo-unified-data-model-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The url-shortener API from Pomo — 2 operation(s) for url-shortener.
  name: Pomo URL Shortener API
  slug: pomo-url-shortener-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The usage API from Pomo — 2 operation(s) for usage.
  name: Pomo Usage API
  slug: pomo-usage-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The user-activity API from Pomo — 4 operation(s) for user-activity.
  name: Pomo User Activity API
  slug: pomo-user-activity-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The user-preferences API from Pomo — 3 operation(s) for user-preferences.
  name: Pomo User Preferences API
  slug: pomo-user-preferences-api
- baseURL: https://api.usepomo.ai
  baseurl_source: declared
  description: The users API from Pomo — 2 operation(s) for users.
  name: Pomo Users API
  slug: pomo-users-api
artifact_total: 105
asyncapis:
- description: ''
  name: Pomo Event Surface
  slug: pomo-event-surface
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/pomo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/pomo-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pomo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usepomo.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pomo-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/pomo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pomo-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://usepomo.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://usepomo.ai/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://usepomo.ai/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://usepomo.ai/
- group: start
  title: ''
  type: SignUp
  url: https://usepomo.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://usepomo.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usepomo.ai/pages/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usepomo.ai/pages/privacy-policy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pomohq/
created: '2026-07-17'
description: Pomo is an AI marketing platform that runs an always-on AI marketing team, turning continuous market, competitor, brand, and trend intelligence into strategy, creative direction, ad-placement planning, and launch-ready campaign workflows for lean growth, brand, and performance teams. It monitors signals daily, surfaces opportunity and whitespace, drafts approval-ready campaigns, briefs, and creatives, and supports AEO/GEO AI-search visibility and Marketing Mix Modeling. Pomo is also offered as a managed service where in-house marketing experts operate the platform on a customer's behalf. The platform runs on a public FastAPI backend at api.usepomo.ai that publishes an OpenAPI 3.1 contract covering 924 paths and 994 operations across campaigns, competitor tracking, market intelligence, earned media, influencer discovery, a unified data model, and connectors to Meta, Google, TikTok, LinkedIn, Shopify, Square, Stripe, QuickBooks, Klaviyo, HubSpot, and Slack, plus a bearer-gated
  programmatic API with self-service API keys and an internal MCP tool broker. The legal entity is MachFlow, Inc. dba Pomo. Founded in 2025 and based in Palo Alto, California, Pomo raised a $4.5M seed round led by Kindred Ventures with Databricks Ventures, SV Angel, and angel investors.
image: https://usepomo.ai/assets/landing-page/cta-demo.png
layout: provider
modified: '2026-08-13'
name: Pomo
nav: Providers
network: true
overview: 'Pomo publishes 100 APIs on the [APIs.io](https://apis.io/) network, including Ab Groups API, Agent Jobs API, Agentic Chat API, and 97 more. Tagged areas include Company, Marketing, Artificial Intelligence, Market Intelligence, and Competitive Intelligence.


  The Pomo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pomo''s developer surface includes engineering blog, support, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Pomo Plans Pricing
  plan_count: 5
  slug: pomo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Pomo Rate Limits
  slug: pomo-rate-limits
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.0
    catalog_earned_first_party: 20.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 61.4
    developer_ergonomics: 37.5
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 48.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 100
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pomo/refs/heads/main/screenshots/pomo-2026-08-17T081321.png
security:
- kind: authentication
  name: Pomo Authentication
  slug: pomo-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Pomo Domain Security
  slug: pomo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pomo
tags:
- Company
- Marketing
- Artificial Intelligence
- Market Intelligence
- Competitive Intelligence
- Marketing Automation
- Generative AI
- Software-as-a-Service
- Answer Engine Optimization
- Advertising
- Social-Media
- Influencer Marketing
- Campaign Management
website: https://usepomo.ai/
---
