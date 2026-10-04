---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.9
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 158
  human_in_the_loop: 3
  name: Aiapplyd Agentic Access
  operation_count: 265
  slug: aiapplyd-agentic-access
  summary_line: 265 operations · 158 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: Hosted remote MCP server (streamable HTTP, with a legacy SSE endpoint; OAuth 2.1 with PKCE, dynamic client registration and Client ID Metadata Documents), version 1.8.0, exposing 17 tools, 4 prompts a
  name: AI Applyd MCP Server
  slug: ai-applyd-mcp-server
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The account API from AI Applyd — 3 operation(s) for account.
  name: AI Applyd Account API
  phrasing_intents:
  - id: getAccount
    intent: Get my account details
    question: What name and phone number are on my account?
  - id: putAccount
    intent: Update my account details
    question: How do I change my name or phone number on my account?
  - id: deleteAccount
    intent: Delete my account permanently
    question: Can I delete my account and all of its data while signed in?
  - id: getAccountExport
    intent: Download an export of my account data
    question: Can I download a copy of all my data?
  - id: postAccountAppleAuthorization
    intent: Store an Apple sign-in authorization
    question: What does the app store after I sign in with Apple?
  phrasing_ops: 5
  slug: aiapplyd-account-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The achievements API from AI Applyd — 1 operation(s) for achievements.
  name: AI Applyd Achievements API
  phrasing_intents:
  - id: getAchievements
    intent: List my achievements
    question: Which achievements have I unlocked in my job search?
  phrasing_ops: 1
  slug: aiapplyd-achievements-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The ai API from AI Applyd — 6 operation(s) for ai.
  name: AI Applyd AI API
  phrasing_intents:
  - id: getAiStatus
    intent: Check my AI auto-apply status and stats
    question: Is the AI applying to jobs for me, and how many has it handled?
  - id: postAiActivate
    intent: Turn on the AI job-application agent
    question: How do I switch on AI applying for my account?
  - id: postAiQualityCheck
    intent: Check if a job passes the quality gate
    question: Would the AI consider a given job good enough to apply to?
  - id: getAiQualityStats
    intent: Get quality gate statistics
    question: How many jobs has the quality gate passed or blocked for me?
  - id: postAiRun
    intent: Run AI on my eligible job matches
    question: Can I make the AI process my eligible matches right now?
  - id: getAiQuota
    intent: Check my AI application quota
    question: How many AI applications do I have left today?
  phrasing_ops: 6
  slug: aiapplyd-ai-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The ai-persona API from AI Applyd — 5 operation(s) for ai-persona.
  name: AI Applyd AI Persona API
  phrasing_intents:
  - id: getAiPersona
    intent: Get my voice and tone settings
    question: What voice and tone is the AI using when it writes for me?
  - id: putAiPersona
    intent: Set my voice, tone and auto-apply rules
    question: How do I change the tone the AI uses in my cover letters?
  - id: patchAiPersonaScoringWeights
    intent: Adjust my match scoring weights
    question: Can I make salary count more than location when jobs are scored for me?
  - id: postAiPersonaSuggestTone
    intent: Recommend a voice preset from my resume
    question: Which voice and tone preset fits my resume best?
  - id: postAiPersonaSuggestNarrative
    intent: Draft a background narrative from my resume
    question: Can AI write a short background story about me from my resume?
  - id: postAiPersonaDeriveCustomTone
    intent: Build a custom voice from my own writing
    question: Can the AI learn my personal writing voice from my resume and cover letter?
  phrasing_ops: 6
  slug: aiapplyd-ai-persona-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The analytics API from AI Applyd — 3 operation(s) for analytics.
  name: AI Applyd Analytics API
  phrasing_intents:
  - id: getAnalytics
    intent: Get my application analytics dashboard
    question: How are my job applications performing overall?
  - id: getAnalyticsPatterns
    intent: Get strategic insights from my applications
    question: What's blocking my applications from converting to interviews?
  - id: postAnalyticsRecommendationsApply
    intent: Apply a pattern-analyzer recommendation
    question: Can I act on one of the recommendations from my application insights?
  phrasing_ops: 3
  slug: aiapplyd-analytics-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The application-profile API from AI Applyd — 2 operation(s) for application-profile.
  name: AI Applyd Application Profile API
  phrasing_intents:
  - id: getApplicationProfile
    intent: Get my job application profile
    question: What details will be used to fill in job applications for me?
  - id: putApplicationProfile
    intent: Update my job application profile
    question: How do I add my LinkedIn and GitHub links to my application profile?
  - id: postApplicationProfileSuggest
    intent: Suggest application fields from my resume
    question: Can my current employer and years of experience be suggested from my resume?
  phrasing_ops: 3
  slug: aiapplyd-application-profile-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The applications API from AI Applyd — 39 operation(s) for applications.
  name: AI Applyd Applications API
  phrasing_intents:
  - id: getApplications
    intent: List my job application results
    question: Which of my auto-applied job applications are still pending review?
  - id: getApplicationsUsage
    intent: Check my rolling 30-day auto-apply cap
    question: How many auto-applies do I have left in my 30-day cap?
  - id: postApplicationsPrepare
    intent: Prepare a tailored resume and cover letter
    question: Can the AI tailor my resume and write a cover letter for one job match?
  - id: postApplicationsResultsApproveBatch
    intent: Bulk approve pending applications
    question: Can I approve a whole batch of pending-review applications at once?
  - id: getApplicationsByIdByResultId
    intent: Get one application result
    question: Where can I see the full details of a single application result?
  - id: postApplicationsByResultIdApprove
    intent: Approve a pending application in copilot mode
    question: How do I approve one application that's waiting for my review in copilot mode?
  - id: postApplicationsByResultIdReject
    intent: Reject a pending application in copilot mode
    question: Can I skip an application the copilot prepared instead of submitting it?
  - id: postApplicationsByResultIdRetry
    intent: Retry a failed submission (admin only)
    question: Can an admin re-queue an application whose submission failed?
  phrasing_ops: 40
  slug: aiapplyd-applications-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The ats API from AI Applyd — 2 operation(s) for ats.
  name: AI Applyd Ats API
  phrasing_intents:
  - id: postAtsScore
    intent: ATS-score pasted resume text
    question: Can I paste plain resume text and get an ATS score back immediately?
  - id: postAtsOptimize
    intent: Rewrite pasted resume text for ATS
    question: Can AI rewrite resume text I paste in so it passes applicant tracking systems?
  phrasing_ops: 2
  slug: aiapplyd-ats-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: Authentication and authorization
  name: AI Applyd Auth API
  phrasing_intents:
  - id: postAuthTestLogin
    intent: Sign in as a local test user
    question: Can I sign in as a test account locally without OAuth?
  phrasing_ops: 1
  slug: aiapplyd-auth-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: Subscription and billing management
  name: AI Applyd Billing API
  phrasing_intents:
  - id: postBillingCreateCheckoutSession
    intent: Start a checkout for a plan or token pack
    question: How do I subscribe or buy a token pack with a card?
  - id: postBillingCreatePortalSession
    intent: Open the billing portal
    question: Where can I update my payment method or manage my subscription?
  - id: postBillingSyncAfterCheckout
    intent: Sync my subscription after checkout
    question: My payment went through but my plan hasn't updated, what can refresh it?
  - id: getBillingSubscription
    intent: Get my subscription and token balance
    question: What plan am I on and how many tokens do I have left?
  - id: postBillingCancelSubscription
    intent: Cancel my subscription
    question: Can I cancel my subscription at the end of the billing period instead of right away?
  - id: postBillingSubscriptionSwitch
    intent: Switch to a different plan
    question: Can I upgrade my plan and pay the prorated difference?
  - id: getBillingInvoices
    intent: List my invoices
    question: Where can I find my past invoices?
  - id: getBillingUsage
    intent: Check per-action usage and limits
    question: How much of each action's quota have I used?
  phrasing_ops: 12
  slug: aiapplyd-billing-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The blog API from AI Applyd — 8 operation(s) for blog.
  name: AI Applyd Blog API
  phrasing_intents:
  - id: getBlogAllContent
    intent: Get every blog post with full content
    question: Can I download every published blog post with its full text at once?
  - id: getBlogPosts
    intent: List blog posts
    question: What are the latest blog posts about job hunting?
  - id: getBlogFeatured
    intent: List featured blog posts
    question: Which blog posts are featured right now?
  - id: getBlogTags
    intent: List blog categories
    question: What categories does the blog cover?
  - id: getBlogTagByTag
    intent: List blog posts in a category
    question: Which blog posts are about resumes?
  - id: getBlogAuthorsBySlug
    intent: Get a blog author and their posts
    question: Who writes the blog and what have they published?
  - id: getBlogPostsBySlug
    intent: Read a blog post
    question: Can I read a single blog article by its slug?
  - id: getBlogPostsBySlugRelated
    intent: Find posts related to a blog post
    question: What other posts are similar to the article I just read?
  phrasing_ops: 8
  slug: aiapplyd-blog-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The companies API from AI Applyd — 2 operation(s) for companies.
  name: AI Applyd Companies API
  phrasing_intents:
  - id: getCompaniesLookup
    intent: Find a company by name
    question: Can I look up a company just by typing its name?
  - id: getCompaniesById
    intent: Get a company profile
    question: What information is on a company's profile?
  phrasing_ops: 2
  slug: aiapplyd-companies-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The dashboard API from AI Applyd — 1 operation(s) for dashboard.
  name: AI Applyd Dashboard API
  phrasing_intents:
  - id: getDashboardBootstrap
    intent: Load everything for my dashboard at once
    question: Can I get my matches, documents, analytics and agent settings in a single call?
  phrasing_ops: 1
  slug: aiapplyd-dashboard-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The email-preferences API from AI Applyd — 3 operation(s) for email-preferences.
  name: AI Applyd Email Preferences API
  phrasing_intents:
  - id: getEmailPreferences
    intent: Get my email subscription settings
    question: Which emails am I currently subscribed to?
  - id: putEmailPreferences
    intent: Change my email subscription settings
    question: How do I stop getting product update emails while signed in?
  - id: getEmailPreferencesByToken
    intent: View email settings from an email link
    question: Can I see my email settings from a link in an email without logging in?
  - id: putEmailPreferencesByToken
    intent: Change email settings from an email link
    question: Can I change which emails I get from the email link without signing in?
  - id: postEmailPreferencesOneClick
    intent: One-click unsubscribe from emails
    question: Does the unsubscribe button in my mail client stop all emails in one click?
  phrasing_ops: 5
  slug: aiapplyd-email-preferences-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The follow-ups API from AI Applyd — 5 operation(s) for follow-ups.
  name: AI Applyd Follow Ups API
  phrasing_intents:
  - id: getFollowUpsHistory
    intent: List follow-ups I've already sent
    question: Which follow-up emails have I sent so far?
  - id: getFollowUps
    intent: List applications due a follow-up
    question: Which applications should I follow up on now?
  - id: getFollowUpsByApplicationIdDraft
    intent: Draft a follow-up email for an application
    question: Can AI write a follow-up email for one of my applications?
  - id: postFollowUpsByApplicationIdSent
    intent: Record a follow-up I sent myself
    question: How do I log a follow-up I sent outside the app?
  - id: postFollowUpsByApplicationIdSendGmail
    intent: Send a follow-up through my Gmail
    question: Can the app send my follow-up email from my connected Gmail?
  phrasing_ops: 5
  slug: aiapplyd-follow-ups-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The integrations API from AI Applyd — 4 operation(s) for integrations.
  name: AI Applyd Integrations API
  phrasing_intents:
  - id: getIntegrationsGoogleConnect
    intent: Start connecting Gmail or Google Calendar
    question: How do I connect my Gmail so replies from employers are tracked?
  - id: getIntegrationsGoogleCallback
    intent: Complete the Google authorization callback
    question: What happens after I approve access on the Google consent screen?
  - id: getIntegrationsGoogleStatus
    intent: Check my Google integration status
    question: Is my Gmail still connected?
  - id: postIntegrationsGoogleDisconnect
    intent: Disconnect Gmail or Google Calendar
    question: How do I unlink my Gmail?
  phrasing_ops: 4
  slug: aiapplyd-integrations-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The job-matches API from AI Applyd — 15 operation(s) for job-matches.
  name: AI Applyd Job Matches API
  phrasing_intents:
  - id: getJobMatchesPreferences
    intent: Get my job match preferences
    question: What roles, locations and salary range are my job matches based on?
  - id: putJobMatchesPreferences
    intent: Update my job match preferences
    question: How do I change the roles and locations I get matched to?
  - id: getJobMatches
    intent: List today's job matches
    question: What jobs has AI matched me with today?
  - id: getJobMatchesWorkStyleSupply
    intent: See how many jobs my work-style choice allows
    question: Why am I seeing so few matches with remote-only selected?
  - id: getJobMatchesById
    intent: Get one job match
    question: Can I pull up the details of a single job match?
  - id: postJobMatchesByIdSave
    intent: Save a job match to my listings
    question: How do I save a job match so it becomes a tracked listing?
  - id: postJobMatchesByIdDismiss
    intent: Dismiss a job match
    question: How do I hide a job match I'm not interested in?
  - id: postJobMatchesSubscribeCell
    intent: Get notified when a role opens in a country
    question: Can I be emailed when jobs for a role family start showing up in my country?
  phrasing_ops: 16
  slug: aiapplyd-job-matches-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The jobs API from AI Applyd — 15 operation(s) for jobs.
  name: AI Applyd Jobs API
  phrasing_intents:
  - id: postJobsExtractKeywords
    intent: Extract ATS keywords from a job description
    question: Which skills and keywords does an ATS look for in a job description?
  - id: postJobsCompare
    intent: Compare several job offers side by side
    question: Can I compare two to five job listings side by side?
  - id: postJobsParseUrl
    intent: Parse a job posting URL into structured data
    question: Can I turn a job posting link into structured job details without saving it?
  - id: postJobsImportUrl
    intent: Import a job into my feed from its apply URL
    question: How do I add a job to my feed from a company's application page link?
  - id: getJobsAtsScoresByAtsScoreId
    intent: Get one ATS score result
    question: Is my ATS score analysis finished yet?
  - id: getJobsStats
    intent: Get my job tracking stats
    question: How many jobs did I apply to today and this week?
  - id: getJobs
    intent: List my tracked job listings
    question: Which jobs am I currently tracking?
  - id: postJobs
    intent: Save a new job listing to track
    question: How do I add a job I found myself so I can track it and score my resume?
  phrasing_ops: 18
  slug: aiapplyd-jobs-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The locations API from AI Applyd — 4 operation(s) for locations.
  name: AI Applyd Locations API
  phrasing_intents:
  - id: getLocationsSearch
    intent: Search cities and places by name
    question: Which cities match what I type into the location box?
  - id: getLocationsPopular
    intent: Browse popular cities by population
    question: What are the biggest cities I can browse when picking locations?
  - id: getLocationsCountries
    intent: Browse countries ranked by population
    question: Which countries can I pick from before drilling into cities?
  - id: getLocationsInitialSuggestions
    intent: Get starter location suggestions
    question: Can the location picker guess my country before I type anything?
  phrasing_ops: 4
  slug: aiapplyd-locations-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The mcp API from AI Applyd — 1 operation(s) for mcp.
  name: AI Applyd MCP API
  phrasing_intents:
  - id: postMcpSession
    intent: Mint a session for an MCP tool user
    question: How does the MCP server get a session token for a user?
  phrasing_ops: 1
  slug: aiapplyd-mcp-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The notifications API from AI Applyd — 5 operation(s) for notifications.
  name: AI Applyd Notifications API
  phrasing_intents:
  - id: postNotificationsPushToken
    intent: Register a device for push notifications
    question: How do I get push notifications on my phone?
  - id: postNotificationsPushTokenUnregister
    intent: Stop push notifications to a device
    question: Should the push token be removed when I sign out on my phone?
  - id: getNotifications
    intent: List my notifications
    question: How many unread notifications do I have?
  - id: patchNotificationsRead
    intent: Mark notifications as read
    question: Can I mark several notifications read at once?
  - id: patchNotificationsDismiss
    intent: Dismiss notifications
    question: Can I dismiss notifications so they leave my feed?
  phrasing_ops: 5
  slug: aiapplyd-notifications-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The observability API from AI Applyd — 1 operation(s) for observability.
  name: AI Applyd Observability API
  phrasing_intents:
  - id: postCspReport
    intent: Report a Content-Security-Policy violation
    question: Where should the browser send Content-Security-Policy violation reports?
  phrasing_ops: 1
  slug: aiapplyd-observability-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The onboarding API from AI Applyd — 8 operation(s) for onboarding.
  name: AI Applyd Onboarding API
  phrasing_intents:
  - id: postOnboardingParseResume
    intent: Parse a resume to start my profile
    question: Can I upload my resume during sign-up and have my profile filled from it?
  - id: postOnboardingAutoSetup
    intent: Set up my account and matches from my resume
    question: Can onboarding create my job preferences and kick off job searches in one step?
  - id: getOnboardingDiscoverStatus
    intent: Check first-time match discovery progress
    question: Is the initial job search after setup still running or did it fail?
  - id: postOnboardingProfile
    intent: Save answers from the onboarding wizard
    question: Can I save my wizard answers one screen at a time?
  - id: getOnboardingProfile
    intent: Get my onboarding wizard answers
    question: What answers did I give in the onboarding wizard?
  - id: getOnboardingResumePrefill
    intent: See which fields came from my resume
    question: Which of my profile fields are still using what was read from my resume?
  - id: postOnboardingComplete
    intent: Finish onboarding
    question: What happens when I complete the setup wizard?
  - id: postOnboardingEscrow
    intent: Hold anonymous setup answers before sign-in
    question: Will my answers survive if I open the magic sign-in link in a different browser?
  phrasing_ops: 9
  slug: aiapplyd-onboarding-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The outreach API from AI Applyd — 4 operation(s) for outreach.
  name: AI Applyd Outreach API
  phrasing_intents:
  - id: getOutreachJobByJobIdContacts
    intent: Get hiring contacts for a saved job
    question: Who should I reach out to at a company for a job I saved but haven't applied to?
  - id: postOutreachJobByJobIdDraft
    intent: Draft an outreach message for a saved job
    question: Can it write a message to a hiring contact for a job I only saved so far?
  - id: getOutreachByApplicationResultIdContacts
    intent: Get hiring contacts for an application
    question: Who are the recruiters at the company I applied to?
  - id: postOutreachByApplicationResultIdDraft
    intent: Draft an outreach message for an application
    question: Can I get a pre-filled email to a recruiter after I've applied?
  phrasing_ops: 4
  slug: aiapplyd-outreach-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The overview API from AI Applyd — 2 operation(s) for overview.
  name: AI Applyd Overview API
  phrasing_intents:
  - id: getOverview
    intent: Get my dashboard overview
    question: What do my dashboard stats look like today?
  - id: getOverviewSuggestions
    intent: Get suggested next steps
    question: What should I do next in my job search?
  phrasing_ops: 2
  slug: aiapplyd-overview-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The pricing API from AI Applyd — 2 operation(s) for pricing.
  name: AI Applyd Pricing API
  phrasing_intents:
  - id: getPricing
    intent: Get all pricing options
    question: How much does AIApplyd cost?
  - id: getPricingSubscriptions
    intent: List subscription plans
    question: Which subscription plans can I sign up for?
  phrasing_ops: 2
  slug: aiapplyd-pricing-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The proof-points API from AI Applyd — 3 operation(s) for proof-points.
  name: AI Applyd Proof Points API
  phrasing_intents:
  - id: getProofPoints
    intent: List my proof points
    question: What achievements do I have in my evidence bank?
  - id: postProofPoints
    intent: Add a proof point to my evidence bank
    question: How do I add an accomplishment with a headline metric to my evidence bank?
  - id: postProofPointsSuggest
    intent: Generate proof points from my resume
    question: Can AI pull accomplishments out of my resume into my evidence bank?
  - id: patchProofPointsById
    intent: Edit a proof point
    question: How do I change the title or metric on an existing proof point?
  - id: deleteProofPointsById
    intent: Delete a proof point
    question: Can I remove a proof point, and is it recoverable afterward?
  phrasing_ops: 5
  slug: aiapplyd-proof-points-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The public-ats-score API from AI Applyd — 2 operation(s) for public-ats-score.
  name: AI Applyd Public Ats Score API
  phrasing_intents:
  - id: postPublicAtsScore
    intent: Get a free ATS score from pasted resume text
    question: Can I check my resume's ATS score for free without signing up?
  - id: postPublicAtsScoreUpload
    intent: Get a free ATS score from an uploaded resume file
    question: Can I upload a PDF or DOCX resume for a free ATS check?
  phrasing_ops: 2
  slug: aiapplyd-public-ats-score-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The public-cancellation API from AI Applyd — 2 operation(s) for public-cancellation.
  name: AI Applyd Public Cancellation API
  phrasing_intents:
  - id: postPublicCancellationRequest
    intent: Email me a one-click cancellation link
    question: How do I cancel my subscription without logging in?
  - id: postPublicCancellationConfirm
    intent: Confirm subscription cancellation
    question: When does my subscription actually end after I confirm cancellation?
  phrasing_ops: 2
  slug: aiapplyd-public-cancellation-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The public-competitors API from AI Applyd — 3 operation(s) for public-competitors.
  name: AI Applyd Public Competitors API
  phrasing_intents:
  - id: getPublicCompetitors
    intent: List published comparison pages
    question: Which tools does AIApplyd publish comparison pages for?
  - id: getPublicCompetitorsBySlug
    intent: Get a comparison page by slug
    question: What does the full head-to-head comparison page for one tool contain?
  - id: getPublicCompetitorsBySlugAlternatives
    intent: List alternatives to a compared tool
    question: What alternatives are listed for a given compared tool, with pros and cons?
  phrasing_ops: 3
  slug: aiapplyd-public-competitors-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The public-deletion API from AI Applyd — 2 operation(s) for public-deletion.
  name: AI Applyd Public Deletion API
  phrasing_intents:
  - id: postPublicDeletionRequest
    intent: Request an account deletion link by email
    question: How do I delete my account if I can't sign in?
  - id: postPublicDeletionConfirm
    intent: Confirm account deletion from the email link
    question: What happens when I click the confirmation link to delete my account?
  phrasing_ops: 2
  slug: aiapplyd-public-deletion-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The public-reviews API from AI Applyd — 1 operation(s) for public-reviews.
  name: AI Applyd Public Reviews API
  phrasing_intents:
  - id: getPublicReviews
    intent: List published customer reviews
    question: What do users say about AI Applyd?
  phrasing_ops: 1
  slug: aiapplyd-public-reviews-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The referrals API from AI Applyd — 3 operation(s) for referrals.
  name: AI Applyd Referrals API
  phrasing_intents:
  - id: getReferralsStats
    intent: Get my referral program stats
    question: How many people signed up through my referral link?
  - id: postReferralsTrack
    intent: Record a click on a referral link
    question: What gets recorded when someone opens a referral link?
  - id: postReferralsConvert
    intent: Credit a signup to a referral
    question: How does a new signup get linked to the person who referred them?
  phrasing_ops: 3
  slug: aiapplyd-referrals-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The relay-inbox API from AI Applyd — 12 operation(s) for relay-inbox.
  name: AI Applyd Relay Inbox API
  phrasing_intents:
  - id: getRelayInbox
    intent: List emails in my job inbox
    question: What recruiter emails have come into my inbox recently?
  - id: getRelayInboxCounts
    intent: Get unread and category counts for my inbox
    question: How many unread emails do I have?
  - id: postRelayInboxBulk
    intent: Apply one action to many inbox emails
    question: Can I archive or mark read a bunch of emails at once?
  - id: getRelayInboxById
    intent: Read one inbox email in full
    question: Can I read the full body of a recruiter's email, including the sender's real address?
  - id: getRelayInboxByIdThread
    intent: View the full conversation for an email
    question: Can I see the whole back-and-forth with a recruiter, including my replies?
  - id: getRelayInboxByIdAttachmentsByPartId
    intent: Download an attachment from an inbox email
    question: How do I download a file a recruiter attached to an email?
  - id: patchRelayInboxByIdCategory
    intent: Correct the category of an inbox email
    question: The classifier marked an interview invite as a rejection — can I fix it?
  - id: patchRelayInboxByIdRead
    intent: Mark an inbox email read or unread
    question: How do I mark one email as unread again?
  phrasing_ops: 13
  slug: aiapplyd-relay-inbox-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The resume-builder API from AI Applyd — 17 operation(s) for resume-builder.
  name: AI Applyd Resume Builder API
  phrasing_intents:
  - id: getResumeBuilder
    intent: List my resume builds
    question: Which resumes have I built so far in the resume builder?
  - id: postResumeBuilder
    intent: Create a new resume build
    question: How do I start a new resume from scratch in the builder?
  - id: getResumeBuilderTemplates
    intent: List available resume templates
    question: What resume templates can I choose from?
  - id: postResumeBuilderImport
    intent: Turn an uploaded document into a resume build
    question: Can AI convert a resume document I already uploaded into an editable structured resume?
  - id: postResumeBuilderByIdImportInline
    intent: Fill an existing resume build from a file
    question: Can I upload a file straight into a resume build I already started and have it filled in?
  - id: getResumeBuilderById
    intent: Get one resume build
    question: What's currently in a specific resume build of mine?
  - id: putResumeBuilderById
    intent: Edit an existing resume build
    question: How do I change the summary or skills on a resume I already built?
  - id: deleteResumeBuilderById
    intent: Delete a resume build
    question: How do I get rid of a resume build I no longer need?
  phrasing_ops: 21
  slug: aiapplyd-resume-builder-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The reviews API from AI Applyd — 1 operation(s) for reviews.
  name: AI Applyd Reviews API
  phrasing_intents:
  - id: getReviewsMe
    intent: Get the review I wrote
    question: Have I already left a review, and has it been approved?
  - id: postReviewsMe
    intent: Write or update my review
    question: How do I leave a star rating and review?
  phrasing_ops: 2
  slug: aiapplyd-reviews-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The saved-searches API from AI Applyd — 2 operation(s) for saved-searches.
  name: AI Applyd Saved Searches API
  phrasing_intents:
  - id: getSavedSearches
    intent: List my saved job searches
    question: Which job alerts have I saved?
  - id: postSavedSearches
    intent: Save a job search with optional alerts
    question: Can I save my current match filters as a named search?
  - id: patchSavedSearchesById
    intent: Rename or change a saved search
    question: Can I turn off email alerts on a saved search without deleting it?
  - id: deleteSavedSearchesById
    intent: Delete a saved search
    question: How do I remove a job alert I no longer want?
  phrasing_ops: 4
  slug: aiapplyd-saved-searches-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The search API from AI Applyd — 2 operation(s) for search.
  name: AI Applyd Search API
  phrasing_intents:
  - id: postSearchDescribe
    intent: Turn a plain-language job search into settings
    question: Can I describe the jobs I want in my own words and get search settings?
  - id: postSearchDescribeFromResume
    intent: Derive job search settings from my resume
    question: Can my job search be set up automatically from my resume?
  phrasing_ops: 2
  slug: aiapplyd-search-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The star-stories API from AI Applyd — 5 operation(s) for star-stories.
  name: AI Applyd Star Stories API
  phrasing_intents:
  - id: getStarStories
    intent: List my STAR interview stories
    question: Which STAR stories have I saved for interviews?
  - id: postStarStories
    intent: Add a STAR story to my bank
    question: How do I save a STAR story I wrote myself for reuse in interviews?
  - id: postStarStoriesDraft
    intent: AI-draft a STAR story for an interview question
    question: Can AI draft a STAR answer to a specific interview question from my resume?
  - id: postStarStoriesGenerateFromResume
    intent: Generate STAR stories from my resume
    question: Can I generate a set of STAR stories from my resume in one click?
  - id: postStarStoriesExtractFromInterviewPrepByJobId
    intent: Extract new STAR stories from interview prep
    question: Which stories from my interview prep for a job aren't in my bank yet?
  - id: patchStarStoriesById
    intent: Edit a STAR story
    question: How do I change the result section of a saved STAR story?
  - id: deleteStarStoriesById
    intent: Delete a STAR story
    question: Can I permanently remove a story from my bank?
  phrasing_ops: 7
  slug: aiapplyd-star-stories-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The support API from AI Applyd — 2 operation(s) for support.
  name: AI Applyd Support API
  phrasing_intents:
  - id: postSupportPublicContentReport
    intent: Report an abusive shared resume or document
    question: How can I report a publicly shared resume that contains my personal info?
  - id: postSupport
    intent: Submit a support ticket or feedback
    question: Where do I file a bug report or feature request?
  phrasing_ops: 2
  slug: aiapplyd-support-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: System health and diagnostics
  name: AI Applyd System API
  phrasing_intents:
  - id: getHealth
    intent: Check that the service is up
    question: Is the API up right now?
  - id: getAuthHealth
    intent: Check my session and plan limits
    question: Is my login session valid, and what plan limits apply to me?
  - id: getAuthCapabilities
    intent: See which sign-in methods are available
    question: Which sign-in options can this deployment actually complete?
  phrasing_ops: 3
  slug: aiapplyd-system-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The tracking API from AI Applyd — 3 operation(s) for tracking.
  name: AI Applyd Tracking API
  phrasing_intents:
  - id: getTrackingActivityFeed
    intent: Get my activity feed across all jobs
    question: What's happened recently across all the jobs I'm tracking?
  - id: getTrackingActivitySummary
    intent: Summarize my last 7 days of activity
    question: How much job search activity did I have this past week?
  - id: getTrackingActivityByJobListingId
    intent: Get the activity timeline for one job
    question: What has happened with one specific job, in order?
  phrasing_ops: 3
  slug: aiapplyd-tracking-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The user-documents API from AI Applyd — 16 operation(s) for user-documents.
  name: AI Applyd User Documents API
  phrasing_intents:
  - id: getUserDocuments
    intent: List my saved documents
    question: Which resumes and cover letters have I uploaded?
  - id: postUserDocuments
    intent: Create a document record
    question: How do I create a new document entry before uploading its file?
  - id: postUserDocumentsTranslatePreview
    intent: Preview a file translation without saving
    question: Can I see what my resume looks like translated before I save anything?
  - id: postUserDocumentsSaveTranslation
    intent: Save a translation preview as a document
    question: How do I keep a translation preview I liked as a real document?
  - id: postUserDocumentsAtsScorePreview
    intent: ATS-score an uploaded file without saving
    question: Can I get an ATS score for a resume file without adding it to my documents?
  - id: postUserDocumentsAtsOptimizePreview
    intent: Preview ATS-optimized content for an upload
    question: Can I see an ATS-optimized version of a resume file before committing to it?
  - id: getUserDocumentsByIdParseStatus
    intent: Check whether a resume has finished parsing
    question: Has the AI finished reading the resume I just uploaded?
  - id: getUserDocumentsById
    intent: Get one saved document
    question: Can I look up the details of a single saved document?
  phrasing_ops: 19
  slug: aiapplyd-user-documents-api
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: The user-preferences API from AI Applyd — 1 operation(s) for user-preferences.
  name: AI Applyd User Preferences API
  phrasing_intents:
  - id: getUserPreferences
    intent: Get my application profile, match prefs and persona
    question: What are my job match preferences and AI persona set to?
  - id: patchUserPreferences
    intent: Update my preferences bundle
    question: Can I update my job match preferences and AI persona in one save?
  phrasing_ops: 2
  slug: aiapplyd-user-preferences-api
- baseURL: https://mcp.aiapplyd.com/mcp
  baseurl_source: declared
  description: The Linked In API from AI Applyd — 3 operation(s) for linked in.
  name: AI Applyd Linked In API
  phrasing_intents:
  - id: postLinkedinImportExport
    intent: Import my LinkedIn profile from a PDF or export
    question: Can I import my LinkedIn profile from the Save to PDF file?
  - id: postLinkedinImportProfile
    intent: Import a LinkedIn profile from its public URL
    question: Can I import my profile just by pasting my LinkedIn URL?
  - id: postLinkedinImportProfileHtml
    intent: Import LinkedIn profile HTML from the extension
    question: How does the Chrome extension import my LinkedIn profile page?
  phrasing_ops: 3
  slug: aiapplyd-linked-in-api
artifact_total: 60
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/well-known/aiapplyd-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aiapplyd-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/well-known/aiapplyd-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aiapplyd-mcp-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/well-known/aiapplyd-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aiapplyd-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/agentic-access/aiapplyd-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aiapplyd-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/rate-limits/aiapplyd-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiapplyd-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/plans/aiapplyd-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiapplyd-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/rules/aiapplyd-rules.yml
  title: ''
  type: Spectral
  url: rules/aiapplyd-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/json-ld/aiapplyd-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aiapplyd-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/vocabulary/aiapplyd-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiapplyd-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/data-model/aiapplyd-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiapplyd-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/changelog/aiapplyd-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aiapplyd-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/conventions/aiapplyd-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aiapplyd-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/conventions/aiapplyd-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aiapplyd-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/authentication/aiapplyd-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiapplyd-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/scopes/aiapplyd-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aiapplyd-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/lifecycle/aiapplyd-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aiapplyd-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/errors/aiapplyd-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiapplyd-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/conformance/aiapplyd-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiapplyd-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/overlays/aiapplyd-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aiapplyd-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/llms/aiapplyd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiapplyd-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/mcp/aiapplyd-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aiapplyd-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/mcp/aiapplyd-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiapplyd-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/well-known/aiapplyd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiapplyd-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/hosts/aiapplyd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiapplyd-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/vendors/aiapplyd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiapplyd-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/packages/aiapplyd-packages.yml
  title: ''
  type: SDKs
  url: packages/aiapplyd-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/packages/aiapplyd-packages.yml
  title: ''
  type: Packages
  url: packages/aiapplyd-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/security/aiapplyd-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aiapplyd-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/security/aiapplyd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiapplyd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiapplyd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aiapplyd.com/mcps
- group: docs
  title: ''
  type: APIReference
  url: https://api.aiapplyd.com/api/v1/scalar
- group: start
  title: ''
  type: GettingStarted
  url: https://aiapplyd.com/mcps
- group: other
  title: ''
  type: APICatalog
  url: https://aiapplyd.com/.well-known/api-catalog
- group: other
  title: ''
  type: ContentSignal
  url: https://aiapplyd.com/robots.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://aiapplyd.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://aiapplyd.com/support
- group: operate
  title: ''
  type: FAQ
  url: https://aiapplyd.com/faq
- group: company
  title: ''
  type: Blog
  url: https://aiapplyd.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aiapplyd
- group: start
  title: ''
  type: SignUp
  url: https://aiapplyd.com/auth/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiapplyd.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiapplyd.com/legal/privacy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://aiapplyd.com/legal/security
created: '2026-09-23'
description: 'AI Applyd is a job-application automation platform for candidates: it scores a resume against a posting for ATS compatibility, rewrites the resume and writes a cover letter per role, prepares interview material, matches new postings to a profile, and fills and submits applications on the employer''s own hiring system across 15 ATS platforms (Workday, Greenhouse, Lever, Ashby, Workable, iCIMS, SmartRecruiters and more), counting an application as sent only when the employer''s system confirms it. It publishes a hosted remote MCP server at mcp.aiapplyd.com/mcp (OAuth 2.1, 17 tools, listed in the official MCP Registry as com.aiapplyd/aiapplyd) with an MIT-licensed stdio bridge on GitHub, and serves the OpenAPI 3.0 description of its application backend at api.aiapplyd.com/api/v1/openapi.json.'
image: https://aiapplyd.com/static/images/logos/icon-logo-dark-square.png
json_schemas:
- name: AutoSetupRequest
  property_count: 23
  slug: aiapplyd-auto-setup-request
- name: PatchUserPreferences
  property_count: 3
  slug: aiapplyd-patch-user-preferences
- name: UpdatePreferencesRequest
  property_count: 19
  slug: aiapplyd-update-preferences-request
- name: UpsertApplicationProfile
  property_count: 34
  slug: aiapplyd-upsert-application-profile
jsonld:
- class_count: 120
  name: Aiapplyd Context
  property_count: 289
  slug: aiapplyd-context
layout: provider
mcp_servers:
- description: ''
  name: AI Applyd
  slug: ai-applyd
modified: '2026-09-25'
name: AI Applyd
nav: Providers
network: true
overview: 'AI Applyd publishes 46 APIs on the [APIs.io](https://apis.io/) network, including Account API, Achievements API, AI API, and 43 more. Tagged areas include Job Search, Recruiting, Resume, Applicant Tracking Systems, and Careers.


  The AI Applyd catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Applyd''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, support, and 38 more developer resources.'
plans:
- name: Aiapplyd Plans Pricing
  plan_count: 3
  slug: aiapplyd-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 6
  name: Aiapplyd Rate Limits
  slug: aiapplyd-rate-limits
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: AI Applyd API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: aiapplyd-rules
scopes:
- name: Aiapplyd Scopes
  scope_count: 0
  slug: aiapplyd-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 74.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 66.2
    developer_ergonomics: 61.9
    discoverability: 91.7
    operational_transparency: 63.2
  previous_composite: 73.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 72.2
security:
- kind: authentication
  name: Aiapplyd Authentication
  slug: aiapplyd-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aiapplyd Domain Security
  slug: aiapplyd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aiapplyd Vulnerability Disclosure
  slug: aiapplyd-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aiapplyd
tags:
- Job Search
- Recruiting
- Resume
- Applicant Tracking Systems
- Careers
- Artificial Intelligence
- MCP
- Automation
website: https://aiapplyd.com/
---
