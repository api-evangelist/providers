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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 927
  human_in_the_loop: 18
  name: Posthog Agentic Access
  operation_count: 1567
  slug: posthog-agentic-access
  summary_line: 1567 operations · 927 acting · 18 human-in-the-loop
api_count: 139
apis:
- description: The PostHog Capture API allows developers to send events, identify users, and set user or group properties from any server or client. It is the primary ingestion endpoint for sending analytics data to
  name: PostHog Capture API
  slug: capture-api
- description: The PostHog Query API provides programmatic access to run HogQL queries against your PostHog data. HogQL is PostHog's SQL-like query language that enables custom analytics queries, funnel analysis, re
  name: PostHog Query API
  slug: query-api
- description: The PostHog Persons API allows developers to retrieve, search, and manage person profiles in PostHog. It supports listing persons with filters, retrieving individual person details, viewing associated
  name: PostHog Persons API
  slug: persons-api
- description: The PostHog Feature Flags API enables developers to create, manage, and evaluate feature flags programmatically. It supports boolean and multivariate flags, percentage-based rollouts, user targeting w
  name: PostHog Feature Flags API
  slug: feature-flags-api
- description: The PostHog Experiments API provides programmatic management of A/B tests and experiments. It supports creating experiments with control and test variants, defining goal metrics, launching and stoppin
  name: PostHog Experiments API
  slug: experiments-api
- description: The PostHog Insights API allows developers to create, retrieve, and manage saved insights such as trends, funnels, retention charts, paths, and lifecycle analyses. It provides programmatic access to t
  name: PostHog Insights API
  slug: insights-api
- description: The PostHog Cohorts API enables developers to create and manage cohorts, which are groups of users defined by shared properties or behavioral patterns. Cohorts can be used for targeting feature flags,
  name: PostHog Cohorts API
  slug: cohorts-api
- description: 'The PostHog Annotations API allows developers to create and manage annotations that mark significant events on PostHog charts and dashboards. Annotations provide context for data changes by recording '
  name: PostHog Annotations API
  slug: annotations-api
- description: The actions API from PostHog — 4 operation(s) for actions.
  name: PostHog actions API
  slug: posthog-actions-api
- description: The activity_log API from PostHog — 1 operation(s) for activity_log.
  name: PostHog activity_log API
  slug: posthog-activity-log-api
- description: The activity_logs API from PostHog — 1 operation(s) for activity_logs.
  name: PostHog activity_logs API
  slug: posthog-activity-logs-api
- description: The advanced_activity_logs API from PostHog — 3 operation(s) for advanced_activity_logs.
  name: PostHog advanced_activity_logs API
  slug: posthog-advanced-activity-logs-api
- description: The alerts API from PostHog — 6 operation(s) for alerts.
  name: PostHog alerts API
  slug: posthog-alerts-api
- description: The annotations API from PostHog — 2 operation(s) for annotations.
  name: PostHog annotations API
  slug: posthog-annotations-api
- description: The approval_policies API from PostHog — 2 operation(s) for approval_policies.
  name: PostHog approval_policies API
  slug: posthog-approval-policies-api
- description: The batch_exports API from PostHog — 40 operation(s) for batch_exports.
  name: PostHog batch_exports API
  slug: posthog-batch-exports-api
- description: The cdp API from PostHog — 23 operation(s) for cdp.
  name: PostHog cdp API
  slug: posthog-cdp-api
- description: The change_requests API from PostHog — 5 operation(s) for change_requests.
  name: PostHog change_requests API
  slug: posthog-change-requests-api
- description: The code API from PostHog — 2 operation(s) for code.
  name: PostHog code API
  slug: posthog-code-api
- description: The code-invites API from PostHog — 2 operation(s) for code-invites.
  name: PostHog code-invites API
  slug: posthog-code-invites-api
- description: The cohorts API from PostHog — 8 operation(s) for cohorts.
  name: PostHog cohorts API
  slug: posthog-cohorts-api
- description: The comments API from PostHog — 4 operation(s) for comments.
  name: PostHog comments API
  slug: posthog-comments-api
- description: The conversations API from PostHog — 14 operation(s) for conversations.
  name: PostHog conversations API
  slug: posthog-conversations-api
- description: The core API from PostHog — 182 operation(s) for core.
  name: PostHog core API
  slug: posthog-core-api
- description: The customer_analytics API from PostHog — 2 operation(s) for customer_analytics.
  name: PostHog customer_analytics API
  slug: posthog-customer-analytics-api
- description: The customer_journeys API from PostHog — 2 operation(s) for customer_journeys.
  name: PostHog customer_journeys API
  slug: posthog-customer-journeys-api
- description: The customer_profile_configs API from PostHog — 2 operation(s) for customer_profile_configs.
  name: PostHog customer_profile_configs API
  slug: posthog-customer-profile-configs-api
- description: The dashboard_templates API from PostHog — 4 operation(s) for dashboard_templates.
  name: PostHog dashboard_templates API
  slug: posthog-dashboard-templates-api
- description: The dashboards API from PostHog — 40 operation(s) for dashboards.
  name: PostHog dashboards API
  slug: posthog-dashboards-api
- description: The data_color_themes API from PostHog — 4 operation(s) for data_color_themes.
  name: PostHog data_color_themes API
  slug: posthog-data-color-themes-api
- description: The data_modeling_jobs API from PostHog — 8 operation(s) for data_modeling_jobs.
  name: PostHog data_modeling_jobs API
  slug: posthog-data-modeling-jobs-api
- description: The data_warehouse API from PostHog — 110 operation(s) for data_warehouse.
  name: PostHog data_warehouse API
  slug: posthog-data-warehouse-api
- description: The dataset_items API from PostHog — 4 operation(s) for dataset_items.
  name: PostHog dataset_items API
  slug: posthog-dataset-items-api
- description: The datasets API from PostHog — 4 operation(s) for datasets.
  name: PostHog datasets API
  slug: posthog-datasets-api
- description: The desktop_recordings API from PostHog — 3 operation(s) for desktop_recordings.
  name: PostHog desktop_recordings API
  slug: posthog-desktop-recordings-api
- description: The domains API from PostHog — 5 operation(s) for domains.
  name: PostHog domains API
  slug: posthog-domains-api
- description: The early_access_feature API from PostHog — 2 operation(s) for early_access_feature.
  name: PostHog early_access_feature API
  slug: posthog-early-access-feature-api
- description: The early_access_features API from PostHog — 2 operation(s) for early_access_features.
  name: PostHog early_access_features API
  slug: posthog-early-access-features-api
- description: The elements API from PostHog — 8 operation(s) for elements.
  name: PostHog elements API
  slug: posthog-elements-api
- description: The endpoints API from PostHog — 16 operation(s) for endpoints.
  name: PostHog endpoints API
  slug: posthog-endpoints-api
- description: The environments API from PostHog — 15 operation(s) for environments.
  name: PostHog environments API
  slug: posthog-environments-api
- description: The error_tracking API from PostHog — 56 operation(s) for error_tracking.
  name: PostHog error_tracking API
  slug: posthog-error-tracking-api
- description: The evaluation_runs API from PostHog — 1 operation(s) for evaluation_runs.
  name: PostHog evaluation_runs API
  slug: posthog-evaluation-runs-api
- description: The evaluations API from PostHog — 3 operation(s) for evaluations.
  name: PostHog evaluations API
  slug: posthog-evaluations-api
- description: The event_definitions API from PostHog — 9 operation(s) for event_definitions.
  name: PostHog event_definitions API
  slug: posthog-event-definitions-api
- description: The event_filter API from PostHog — 3 operation(s) for event_filter.
  name: PostHog event_filter API
  slug: posthog-event-filter-api
- description: The event_schemas API from PostHog — 2 operation(s) for event_schemas.
  name: PostHog event_schemas API
  slug: posthog-event-schemas-api
- description: The events API from PostHog — 6 operation(s) for events.
  name: PostHog events API
  slug: posthog-events-api
- description: The experiment_holdouts API from PostHog — 2 operation(s) for experiment_holdouts.
  name: PostHog experiment_holdouts API
  slug: posthog-experiment-holdouts-api
- description: The experiment_saved_metrics API from PostHog — 2 operation(s) for experiment_saved_metrics.
  name: PostHog experiment_saved_metrics API
  slug: posthog-experiment-saved-metrics-api
- description: The experiments API from PostHog — 18 operation(s) for experiments.
  name: PostHog experiments API
  slug: posthog-experiments-api
- description: The exports API from PostHog — 6 operation(s) for exports.
  name: PostHog exports API
  slug: posthog-exports-api
- description: The external_data_schemas API from PostHog — 14 operation(s) for external_data_schemas.
  name: PostHog external_data_schemas API
  slug: posthog-external-data-schemas-api
- description: The external_data_sources API from PostHog — 32 operation(s) for external_data_sources.
  name: PostHog external_data_sources API
  slug: posthog-external-data-sources-api
- description: The feature_flags API from PostHog — 19 operation(s) for feature_flags.
  name: PostHog feature_flags API
  slug: posthog-feature-flags-api
- description: The file_system API from PostHog — 18 operation(s) for file_system.
  name: PostHog file_system API
  slug: posthog-file-system-api
- description: The file_system_shortcut API from PostHog — 6 operation(s) for file_system_shortcut.
  name: PostHog file_system_shortcut API
  slug: posthog-file-system-shortcut-api
- description: The flag_value API from PostHog — 1 operation(s) for flag_value.
  name: PostHog flag_value API
  slug: posthog-flag-value-api
- description: The groups API from PostHog — 16 operation(s) for groups.
  name: PostHog groups API
  slug: posthog-groups-api
- description: The groups_types API from PostHog — 7 operation(s) for groups_types.
  name: PostHog groups_types API
  slug: posthog-groups-types-api
- description: The health_issues API from PostHog — 4 operation(s) for health_issues.
  name: PostHog health_issues API
  slug: posthog-health-issues-api
- description: The heatmap_screenshots API from PostHog — 2 operation(s) for heatmap_screenshots.
  name: PostHog heatmap_screenshots API
  slug: posthog-heatmap-screenshots-api
- description: The heatmaps API from PostHog — 4 operation(s) for heatmaps.
  name: PostHog heatmaps API
  slug: posthog-heatmaps-api
- description: The hog_flows API from PostHog — 28 operation(s) for hog_flows.
  name: PostHog hog_flows API
  slug: posthog-hog-flows-api
- description: The hog_function_templates API from PostHog — 3 operation(s) for hog_function_templates.
  name: PostHog hog_function_templates API
  slug: posthog-hog-function-templates-api
- description: The hog_functions API from PostHog — 20 operation(s) for hog_functions.
  name: PostHog hog_functions API
  slug: posthog-hog-functions-api
- description: The insight_variables API from PostHog — 4 operation(s) for insight_variables.
  name: PostHog insight_variables API
  slug: posthog-insight-variables-api
- description: The insights API from PostHog — 36 operation(s) for insights.
  name: PostHog insights API
  slug: posthog-insights-api
- description: The integrations API from PostHog — 52 operation(s) for integrations.
  name: PostHog integrations API
  slug: posthog-integrations-api
- description: The invites API from PostHog — 3 operation(s) for invites.
  name: PostHog invites API
  slug: posthog-invites-api
- description: The js-snippet API from PostHog — 2 operation(s) for js-snippet.
  name: PostHog js-snippet API
  slug: posthog-js-snippet-api
- description: The legal_documents API from PostHog — 3 operation(s) for legal_documents.
  name: PostHog legal_documents API
  slug: posthog-legal-documents-api
- description: The lineage API from PostHog — 1 operation(s) for lineage.
  name: PostHog lineage API
  slug: posthog-lineage-api
- description: The live_debugger_breakpoints API from PostHog — 4 operation(s) for live_debugger_breakpoints.
  name: PostHog live_debugger_breakpoints API
  slug: posthog-live-debugger-breakpoints-api
- description: The LLM Analytics API from PostHog — 58 operation(s) for llm analytics.
  name: PostHog LLM Analytics API
  slug: posthog-llm-analytics-api
- description: The llm_prompts API from PostHog — 5 operation(s) for llm_prompts.
  name: PostHog llm_prompts API
  slug: posthog-llm-prompts-api
- description: The llm_skills API from PostHog — 8 operation(s) for llm_skills.
  name: PostHog llm_skills API
  slug: posthog-llm-skills-api
- description: The logs API from PostHog — 43 operation(s) for logs.
  name: PostHog logs API
  slug: posthog-logs-api
- description: The managed_viewsets API from PostHog — 1 operation(s) for managed_viewsets.
  name: PostHog managed_viewsets API
  slug: posthog-managed-viewsets-api
- description: The max API from PostHog — 7 operation(s) for max.
  name: PostHog max API
  slug: posthog-max-api
- description: The max_tools API from PostHog — 1 operation(s) for max_tools.
  name: PostHog max_tools API
  slug: posthog-max-tools-api
- description: The mcp_server_installations API from PostHog — 9 operation(s) for mcp_server_installations.
  name: PostHog mcp_server_installations API
  slug: posthog-mcp-server-installations-api
- description: The mcp_servers API from PostHog — 1 operation(s) for mcp_servers.
  name: PostHog mcp_servers API
  slug: posthog-mcp-servers-api
- description: The mcp_store API from PostHog — 10 operation(s) for mcp_store.
  name: PostHog mcp_store API
  slug: posthog-mcp-store-api
- description: The mcp_tools API from PostHog — 1 operation(s) for mcp_tools.
  name: PostHog mcp_tools API
  slug: posthog-mcp-tools-api
- description: The members API from PostHog — 3 operation(s) for members.
  name: PostHog members API
  slug: posthog-members-api
- description: The notebooks API from PostHog — 16 operation(s) for notebooks.
  name: PostHog notebooks API
  slug: posthog-notebooks-api
- description: The oauth_applications API from PostHog — 1 operation(s) for oauth_applications.
  name: PostHog oauth_applications API
  slug: posthog-oauth-applications-api
- description: The object_media_previews API from PostHog — 3 operation(s) for object_media_previews.
  name: PostHog object_media_previews API
  slug: posthog-object-media-previews-api
- description: The organizations API from PostHog — 5 operation(s) for organizations.
  name: PostHog organizations API
  slug: posthog-organizations-api
- description: The persisted_folder API from PostHog — 4 operation(s) for persisted_folder.
  name: PostHog persisted_folder API
  slug: posthog-persisted-folder-api
- description: The persons API from PostHog — 40 operation(s) for persons.
  name: PostHog persons API
  slug: posthog-persons-api
- description: The platform_features API from PostHog — 26 operation(s) for platform_features.
  name: PostHog platform_features API
  slug: posthog-platform-features-api
- description: The plugin_configs API from PostHog — 2 operation(s) for plugin_configs.
  name: PostHog plugin_configs API
  slug: posthog-plugin-configs-api
- description: The product_analytics API from PostHog — 32 operation(s) for product_analytics.
  name: PostHog product_analytics API
  slug: posthog-product-analytics-api
- description: The product_tours API from PostHog — 7 operation(s) for product_tours.
  name: PostHog product_tours API
  slug: posthog-product-tours-api
- description: The project_secret_api_keys API from PostHog — 6 operation(s) for project_secret_api_keys.
  name: PostHog project_secret_api_keys API
  slug: posthog-project-secret-api-keys-api
- description: The projects API from PostHog — 11 operation(s) for projects.
  name: PostHog projects API
  slug: posthog-projects-api
- description: The property_definitions API from PostHog — 4 operation(s) for property_definitions.
  name: PostHog property_definitions API
  slug: posthog-property-definitions-api
- description: The proxy_records API from PostHog — 3 operation(s) for proxy_records.
  name: PostHog proxy_records API
  slug: posthog-proxy-records-api
- description: The public_hog_function_templates API from PostHog — 1 operation(s) for public_hog_function_templates.
  name: PostHog public_hog_function_templates API
  slug: posthog-public-hog-function-templates-api
- description: The query API from PostHog — 14 operation(s) for query.
  name: PostHog query API
  slug: posthog-query-api
- description: The replay API from PostHog — 13 operation(s) for replay.
  name: PostHog replay API
  slug: posthog-replay-api
- description: The reverse_proxy API from PostHog — 3 operation(s) for reverse_proxy.
  name: PostHog reverse_proxy API
  slug: posthog-reverse-proxy-api
- description: The role_external_references API from PostHog — 3 operation(s) for role_external_references.
  name: PostHog role_external_references API
  slug: posthog-role-external-references-api
- description: The roles API from PostHog — 4 operation(s) for roles.
  name: PostHog roles API
  slug: posthog-roles-api
- description: The sandbox-environments API from PostHog — 2 operation(s) for sandbox-environments.
  name: PostHog sandbox-environments API
  slug: posthog-sandbox-environments-api
- description: The saved API from PostHog — 6 operation(s) for saved.
  name: PostHog saved API
  slug: posthog-saved-api
- description: The schema_property_groups API from PostHog — 2 operation(s) for schema_property_groups.
  name: PostHog schema_property_groups API
  slug: posthog-schema-property-groups-api
- description: The sdk_doctor API from PostHog — 1 operation(s) for sdk_doctor.
  name: PostHog sdk_doctor API
  slug: posthog-sdk-doctor-api
- description: The session_group_summaries API from PostHog — 2 operation(s) for session_group_summaries.
  name: PostHog session_group_summaries API
  slug: posthog-session-group-summaries-api
- description: The session_recording_playlists API from PostHog — 8 operation(s) for session_recording_playlists.
  name: PostHog session_recording_playlists API
  slug: posthog-session-recording-playlists-api
- description: The session_recordings API from PostHog — 12 operation(s) for session_recordings.
  name: PostHog session_recordings API
  slug: posthog-session-recordings-api
- description: The session_summaries API from PostHog — 3 operation(s) for session_summaries.
  name: PostHog session_summaries API
  slug: posthog-session-summaries-api
- description: The sessions API from PostHog — 4 operation(s) for sessions.
  name: PostHog sessions API
  slug: posthog-sessions-api
- description: The signals API from PostHog — 6 operation(s) for signals.
  name: PostHog signals API
  slug: posthog-signals-api
- description: The subscriptions API from PostHog — 8 operation(s) for subscriptions.
  name: PostHog subscriptions API
  slug: posthog-subscriptions-api
- description: The surveys API from PostHog — 14 operation(s) for surveys.
  name: PostHog surveys API
  slug: posthog-surveys-api
- description: The taggers API from PostHog — 3 operation(s) for taggers.
  name: PostHog taggers API
  slug: posthog-taggers-api
- description: The task-automations API from PostHog — 3 operation(s) for task-automations.
  name: PostHog task-automations API
  slug: posthog-task-automations-api
- description: The task-runs API from PostHog — 17 operation(s) for task-runs.
  name: PostHog task-runs API
  slug: posthog-task-runs-api
- description: The tasks API from PostHog — 24 operation(s) for tasks.
  name: PostHog tasks API
  slug: posthog-tasks-api
- description: The uploaded_media API from PostHog — 1 operation(s) for uploaded_media.
  name: PostHog uploaded_media API
  slug: posthog-uploaded-media-api
- description: The user_home_settings API from PostHog — 1 operation(s) for user_home_settings.
  name: PostHog user_home_settings API
  slug: posthog-user-home-settings-api
- description: The user_interviews API from PostHog — 2 operation(s) for user_interviews.
  name: PostHog user_interviews API
  slug: posthog-user-interviews-api
- description: The users API from PostHog — 22 operation(s) for users.
  name: PostHog users API
  slug: posthog-users-api
- description: The visual_review API from PostHog — 22 operation(s) for visual_review.
  name: PostHog visual_review API
  slug: posthog-visual-review-api
- description: The warehouse_dag API from PostHog — 1 operation(s) for warehouse_dag.
  name: PostHog warehouse_dag API
  slug: posthog-warehouse-dag-api
- description: The warehouse_model_paths API from PostHog — 2 operation(s) for warehouse_model_paths.
  name: PostHog warehouse_model_paths API
  slug: posthog-warehouse-model-paths-api
- description: The warehouse_saved_queries API from PostHog — 24 operation(s) for warehouse_saved_queries.
  name: PostHog warehouse_saved_queries API
  slug: posthog-warehouse-saved-queries-api
- description: The warehouse_saved_query_folders API from PostHog — 4 operation(s) for warehouse_saved_query_folders.
  name: PostHog warehouse_saved_query_folders API
  slug: posthog-warehouse-saved-query-folders-api
- description: The warehouse_tables API from PostHog — 10 operation(s) for warehouse_tables.
  name: PostHog warehouse_tables API
  slug: posthog-warehouse-tables-api
- description: The warehouse_view_link API from PostHog — 6 operation(s) for warehouse_view_link.
  name: PostHog warehouse_view_link API
  slug: posthog-warehouse-view-link-api
- description: The warehouse_view_links API from PostHog — 6 operation(s) for warehouse_view_links.
  name: PostHog warehouse_view_links API
  slug: posthog-warehouse-view-links-api
- description: The web_analytics API from PostHog — 1 operation(s) for web_analytics.
  name: PostHog web_analytics API
  slug: posthog-web-analytics-api
- description: The web_experiments API from PostHog — 2 operation(s) for web_experiments.
  name: PostHog web_experiments API
  slug: posthog-web-experiments-api
- description: The web_vitals API from PostHog — 1 operation(s) for web_vitals.
  name: PostHog web_vitals API
  slug: posthog-web-vitals-api
- description: The welcome API from PostHog — 1 operation(s) for welcome.
  name: PostHog welcome API
  slug: posthog-welcome-api
- description: The workflows API from PostHog — 28 operation(s) for workflows.
  name: PostHog workflows API
  slug: posthog-workflows-api
artifact_total: 1909
asyncapis:
- description: 'PostHog''s Customer Data Platform (CDP) exposes a webhook destination that sends event and person data from PostHog to any external HTTP endpoint in real time. The generic Webhook destination supports '
  name: PostHog Webhook Destinations
  slug: posthog-webhooks-asyncapi
collections:
- collection_type: postman
  name: PostHog actions API
  slug: postman-posthog-actions-api
- collection_type: postman
  name: PostHog actions activity_log API
  slug: postman-posthog-activity-log-api
- collection_type: postman
  name: PostHog actions activity_logs API
  slug: postman-posthog-activity-logs-api
- collection_type: postman
  name: PostHog actions advanced_activity_logs API
  slug: postman-posthog-advanced-activity-logs-api
- collection_type: postman
  name: PostHog actions alerts API
  slug: postman-posthog-alerts-api
- collection_type: postman
  name: PostHog actions annotations API
  slug: postman-posthog-annotations-api
- collection_type: postman
  name: PostHog actions approval_policies API
  slug: postman-posthog-approval-policies-api
- collection_type: postman
  name: PostHog actions batch_exports API
  slug: postman-posthog-batch-exports-api
- collection_type: postman
  name: PostHog actions cdp API
  slug: postman-posthog-cdp-api
- collection_type: postman
  name: PostHog actions change_requests API
  slug: postman-posthog-change-requests-api
- collection_type: postman
  name: PostHog actions code API
  slug: postman-posthog-code-api
- collection_type: postman
  name: PostHog actions code-invites API
  slug: postman-posthog-code-invites-api
- collection_type: postman
  name: PostHog actions cohorts API
  slug: postman-posthog-cohorts-api
- collection_type: postman
  name: PostHog actions comments API
  slug: postman-posthog-comments-api
- collection_type: postman
  name: PostHog actions conversations API
  slug: postman-posthog-conversations-api
- collection_type: postman
  name: PostHog actions core API
  slug: postman-posthog-core-api
- collection_type: postman
  name: PostHog actions customer_analytics API
  slug: postman-posthog-customer-analytics-api
- collection_type: postman
  name: PostHog actions customer_journeys API
  slug: postman-posthog-customer-journeys-api
- collection_type: postman
  name: PostHog actions customer_profile_configs API
  slug: postman-posthog-customer-profile-configs-api
- collection_type: postman
  name: PostHog actions dashboard_templates API
  slug: postman-posthog-dashboard-templates-api
- collection_type: postman
  name: PostHog actions dashboards API
  slug: postman-posthog-dashboards-api
- collection_type: postman
  name: PostHog actions data_color_themes API
  slug: postman-posthog-data-color-themes-api
- collection_type: postman
  name: PostHog actions data_modeling_jobs API
  slug: postman-posthog-data-modeling-jobs-api
- collection_type: postman
  name: PostHog actions data_warehouse API
  slug: postman-posthog-data-warehouse-api
- collection_type: postman
  name: PostHog actions dataset_items API
  slug: postman-posthog-dataset-items-api
- collection_type: postman
  name: PostHog actions datasets API
  slug: postman-posthog-datasets-api
- collection_type: postman
  name: PostHog actions desktop_recordings API
  slug: postman-posthog-desktop-recordings-api
- collection_type: postman
  name: PostHog actions domains API
  slug: postman-posthog-domains-api
- collection_type: postman
  name: PostHog actions early_access_feature API
  slug: postman-posthog-early-access-feature-api
- collection_type: postman
  name: PostHog actions early_access_features API
  slug: postman-posthog-early-access-features-api
- collection_type: postman
  name: PostHog actions elements API
  slug: postman-posthog-elements-api
- collection_type: postman
  name: PostHog actions endpoints API
  slug: postman-posthog-endpoints-api
- collection_type: postman
  name: PostHog actions environments API
  slug: postman-posthog-environments-api
- collection_type: postman
  name: PostHog actions error_tracking API
  slug: postman-posthog-error-tracking-api
- collection_type: postman
  name: PostHog actions evaluation_runs API
  slug: postman-posthog-evaluation-runs-api
- collection_type: postman
  name: PostHog actions evaluations API
  slug: postman-posthog-evaluations-api
- collection_type: postman
  name: PostHog actions event_definitions API
  slug: postman-posthog-event-definitions-api
- collection_type: postman
  name: PostHog actions event_filter API
  slug: postman-posthog-event-filter-api
- collection_type: postman
  name: PostHog actions event_schemas API
  slug: postman-posthog-event-schemas-api
- collection_type: postman
  name: PostHog actions events API
  slug: postman-posthog-events-api
- collection_type: postman
  name: PostHog actions experiment_holdouts API
  slug: postman-posthog-experiment-holdouts-api
- collection_type: postman
  name: PostHog actions experiment_saved_metrics API
  slug: postman-posthog-experiment-saved-metrics-api
- collection_type: postman
  name: PostHog actions experiments API
  slug: postman-posthog-experiments-api
- collection_type: postman
  name: PostHog actions exports API
  slug: postman-posthog-exports-api
- collection_type: postman
  name: PostHog actions external_data_schemas API
  slug: postman-posthog-external-data-schemas-api
- collection_type: postman
  name: PostHog actions external_data_sources API
  slug: postman-posthog-external-data-sources-api
- collection_type: postman
  name: PostHog actions feature_flags API
  slug: postman-posthog-feature-flags-api
- collection_type: postman
  name: PostHog actions file_system API
  slug: postman-posthog-file-system-api
- collection_type: postman
  name: PostHog actions file_system_shortcut API
  slug: postman-posthog-file-system-shortcut-api
- collection_type: postman
  name: PostHog actions flag_value API
  slug: postman-posthog-flag-value-api
- collection_type: postman
  name: PostHog actions groups API
  slug: postman-posthog-groups-api
- collection_type: postman
  name: PostHog actions groups_types API
  slug: postman-posthog-groups-types-api
- collection_type: postman
  name: PostHog actions health_issues API
  slug: postman-posthog-health-issues-api
- collection_type: postman
  name: PostHog actions heatmap_screenshots API
  slug: postman-posthog-heatmap-screenshots-api
- collection_type: postman
  name: PostHog actions heatmaps API
  slug: postman-posthog-heatmaps-api
- collection_type: postman
  name: PostHog actions hog_flows API
  slug: postman-posthog-hog-flows-api
- collection_type: postman
  name: PostHog actions hog_function_templates API
  slug: postman-posthog-hog-function-templates-api
- collection_type: postman
  name: PostHog actions hog_functions API
  slug: postman-posthog-hog-functions-api
- collection_type: postman
  name: PostHog actions insight_variables API
  slug: postman-posthog-insight-variables-api
- collection_type: postman
  name: PostHog actions insights API
  slug: postman-posthog-insights-api
- collection_type: postman
  name: PostHog actions integrations API
  slug: postman-posthog-integrations-api
- collection_type: postman
  name: PostHog actions invites API
  slug: postman-posthog-invites-api
- collection_type: postman
  name: PostHog actions js-snippet API
  slug: postman-posthog-js-snippet-api
- collection_type: postman
  name: PostHog actions legal_documents API
  slug: postman-posthog-legal-documents-api
- collection_type: postman
  name: PostHog actions lineage API
  slug: postman-posthog-lineage-api
- collection_type: postman
  name: PostHog actions live_debugger_breakpoints API
  slug: postman-posthog-live-debugger-breakpoints-api
- collection_type: postman
  name: PostHog actions LLM Analytics API
  slug: postman-posthog-llm-analytics-api
- collection_type: postman
  name: PostHog actions llm_prompts API
  slug: postman-posthog-llm-prompts-api
- collection_type: postman
  name: PostHog actions llm_skills API
  slug: postman-posthog-llm-skills-api
- collection_type: postman
  name: PostHog actions logs API
  slug: postman-posthog-logs-api
- collection_type: postman
  name: PostHog actions managed_viewsets API
  slug: postman-posthog-managed-viewsets-api
- collection_type: postman
  name: PostHog actions max API
  slug: postman-posthog-max-api
- collection_type: postman
  name: PostHog actions max_tools API
  slug: postman-posthog-max-tools-api
- collection_type: postman
  name: PostHog actions mcp_server_installations API
  slug: postman-posthog-mcp-server-installations-api
- collection_type: postman
  name: PostHog actions mcp_servers API
  slug: postman-posthog-mcp-servers-api
- collection_type: postman
  name: PostHog actions mcp_store API
  slug: postman-posthog-mcp-store-api
- collection_type: postman
  name: PostHog actions mcp_tools API
  slug: postman-posthog-mcp-tools-api
- collection_type: postman
  name: PostHog actions members API
  slug: postman-posthog-members-api
- collection_type: postman
  name: PostHog actions notebooks API
  slug: postman-posthog-notebooks-api
- collection_type: postman
  name: PostHog actions oauth_applications API
  slug: postman-posthog-oauth-applications-api
- collection_type: postman
  name: PostHog actions object_media_previews API
  slug: postman-posthog-object-media-previews-api
- collection_type: postman
  name: PostHog actions organizations API
  slug: postman-posthog-organizations-api
- collection_type: postman
  name: PostHog actions persisted_folder API
  slug: postman-posthog-persisted-folder-api
- collection_type: postman
  name: PostHog actions persons API
  slug: postman-posthog-persons-api
- collection_type: postman
  name: PostHog actions platform_features API
  slug: postman-posthog-platform-features-api
- collection_type: postman
  name: PostHog actions plugin_configs API
  slug: postman-posthog-plugin-configs-api
- collection_type: postman
  name: PostHog actions product_analytics API
  slug: postman-posthog-product-analytics-api
- collection_type: postman
  name: PostHog actions product_tours API
  slug: postman-posthog-product-tours-api
- collection_type: postman
  name: PostHog actions project_secret_api_keys API
  slug: postman-posthog-project-secret-api-keys-api
- collection_type: postman
  name: PostHog actions projects API
  slug: postman-posthog-projects-api
- collection_type: postman
  name: PostHog actions property_definitions API
  slug: postman-posthog-property-definitions-api
- collection_type: postman
  name: PostHog actions proxy_records API
  slug: postman-posthog-proxy-records-api
- collection_type: postman
  name: PostHog actions public_hog_function_templates API
  slug: postman-posthog-public-hog-function-templates-api
- collection_type: postman
  name: PostHog actions query API
  slug: postman-posthog-query-api
- collection_type: postman
  name: PostHog actions replay API
  slug: postman-posthog-replay-api
- collection_type: postman
  name: PostHog actions reverse_proxy API
  slug: postman-posthog-reverse-proxy-api
- collection_type: postman
  name: PostHog actions role_external_references API
  slug: postman-posthog-role-external-references-api
- collection_type: postman
  name: PostHog actions roles API
  slug: postman-posthog-roles-api
- collection_type: postman
  name: PostHog actions sandbox-environments API
  slug: postman-posthog-sandbox-environments-api
- collection_type: postman
  name: PostHog actions saved API
  slug: postman-posthog-saved-api
- collection_type: postman
  name: PostHog actions schema_property_groups API
  slug: postman-posthog-schema-property-groups-api
- collection_type: postman
  name: PostHog actions sdk_doctor API
  slug: postman-posthog-sdk-doctor-api
- collection_type: postman
  name: PostHog actions session_group_summaries API
  slug: postman-posthog-session-group-summaries-api
- collection_type: postman
  name: PostHog actions session_recording_playlists API
  slug: postman-posthog-session-recording-playlists-api
- collection_type: postman
  name: PostHog actions session_recordings API
  slug: postman-posthog-session-recordings-api
- collection_type: postman
  name: PostHog actions session_summaries API
  slug: postman-posthog-session-summaries-api
- collection_type: postman
  name: PostHog actions sessions API
  slug: postman-posthog-sessions-api
- collection_type: postman
  name: PostHog actions signals API
  slug: postman-posthog-signals-api
- collection_type: postman
  name: PostHog actions subscriptions API
  slug: postman-posthog-subscriptions-api
- collection_type: postman
  name: PostHog actions surveys API
  slug: postman-posthog-surveys-api
- collection_type: postman
  name: PostHog actions taggers API
  slug: postman-posthog-taggers-api
- collection_type: postman
  name: PostHog actions task-automations API
  slug: postman-posthog-task-automations-api
- collection_type: postman
  name: PostHog actions task-runs API
  slug: postman-posthog-task-runs-api
- collection_type: postman
  name: PostHog actions tasks API
  slug: postman-posthog-tasks-api
- collection_type: postman
  name: PostHog actions uploaded_media API
  slug: postman-posthog-uploaded-media-api
- collection_type: postman
  name: PostHog actions user_home_settings API
  slug: postman-posthog-user-home-settings-api
- collection_type: postman
  name: PostHog actions user_interviews API
  slug: postman-posthog-user-interviews-api
- collection_type: postman
  name: PostHog actions users API
  slug: postman-posthog-users-api
- collection_type: postman
  name: PostHog actions visual_review API
  slug: postman-posthog-visual-review-api
- collection_type: postman
  name: PostHog actions warehouse_dag API
  slug: postman-posthog-warehouse-dag-api
- collection_type: postman
  name: PostHog actions warehouse_model_paths API
  slug: postman-posthog-warehouse-model-paths-api
- collection_type: postman
  name: PostHog actions warehouse_saved_queries API
  slug: postman-posthog-warehouse-saved-queries-api
- collection_type: postman
  name: PostHog actions warehouse_saved_query_folders API
  slug: postman-posthog-warehouse-saved-query-folders-api
- collection_type: postman
  name: PostHog actions warehouse_tables API
  slug: postman-posthog-warehouse-tables-api
- collection_type: postman
  name: PostHog actions warehouse_view_link API
  slug: postman-posthog-warehouse-view-link-api
- collection_type: postman
  name: PostHog actions warehouse_view_links API
  slug: postman-posthog-warehouse-view-links-api
- collection_type: postman
  name: PostHog actions web_analytics API
  slug: postman-posthog-web-analytics-api
- collection_type: postman
  name: PostHog actions web_experiments API
  slug: postman-posthog-web-experiments-api
- collection_type: postman
  name: PostHog actions web_vitals API
  slug: postman-posthog-web-vitals-api
- collection_type: postman
  name: PostHog actions welcome API
  slug: postman-posthog-welcome-api
- collection_type: postman
  name: PostHog actions workflows API
  slug: postman-posthog-workflows-api
- collection_type: open
  name: PostHog API
  slug: open-posthog
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/posthog/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/posthog-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/posthog-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/posthog-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/posthog-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/posthog-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/posthog
- group: company
  title: ''
  type: Website
  url: https://posthog.com
- group: docs
  title: ''
  type: Documentation
  url: https://posthog.com/docs
- group: docs
  title: ''
  type: APIDocumentation
  url: https://posthog.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://posthog.com/docs/getting-started/install
- group: company
  title: ''
  type: Blog
  url: https://posthog.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://posthog.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/PostHog/posthog
- group: start
  title: ''
  type: Login
  url: https://app.posthog.com/login
- group: start
  title: ''
  type: Signup
  url: https://app.posthog.com/signup
- group: operate
  title: ''
  type: Support
  url: https://posthog.com/questions
- group: operate
  title: ''
  type: ChangeLog
  url: https://posthog.com/changelog
- group: build
  title: ''
  type: SDKs
  url: https://posthog.com/docs/libraries
- group: other
  title: ''
  type: SelfHosted
  url: https://posthog.com/docs/self-host
- group: operate
  title: ''
  type: StatusPage
  url: https://status.posthog.com
- group: operate
  title: ''
  type: Slack
  url: https://posthog.com/slack
- group: commercial
  title: ''
  type: TermsOfService
  url: https://posthog.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://posthog.com/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://posthog.com/llms.txt
created: '2026-03-26'
description: PostHog is an open source product analytics platform that provides event tracking, session recording, feature flags, A/B testing, and user surveys in a single platform. It can be self-hosted or used as a cloud service, giving teams full control over their product data while providing comprehensive tools for understanding and improving user experiences.
examples:
- key_count: 6
  name: Posthog Llm Analytics Evaluation Summary Create Example
  slug: posthog-llm-analytics-evaluation-summary-create-example
- key_count: 6
  name: Posthog Llm Analytics Summarization Create Example
  slug: posthog-llm-analytics-summarization-create-example
- key_count: 6
  name: Posthog Llm Analytics Text Repr Create Example
  slug: posthog-llm-analytics-text-repr-create-example
features:
- 'Product Analytics: 1M events free, tiered $0.0000500-$0.0000090 per event'
- 'Session Replay: 5K replays free, tiered $0.005-$0.0015 per replay'
- 'Feature Flags + Experiments: 1M requests free, tiered down to $0.00001'
- 'Enterprise: SAML/RBAC/audit logs as add-on'
- Open-source self-hosted alternative (PostHog Cloud or self-host)
- Capture API for events from web/mobile/server
- HogQL (SQL-style query language)
- Decide API for flag evaluation
- 'Public API: 240 req/min/user'
- Auto-capture for click/page-view tracking
- Webhooks for actions and cohort changes
- Personal API keys + project keys
- 'SDK ecosystem: JS, React, mobile, server (10+)'
- Surveys, A/B tests, multivariate experiments
- Data warehouse integration (BigQuery, Snowflake, Redshift)
- EU + US data residency
finops:
- name: Posthog Finops
  service_category: Product Analytics
  slug: posthog-finops
graphqls:
- description: PostHog does not expose a public GraphQL endpoint. Its primary API surface is a REST API documented at https://posthog.com/docs/api, with an additional HogQL query layer (SQL-like) accessible via `POS
  name: PostHog GraphQL Schema
  slug: posthog-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/posthog.png
json_schemas:
- name: AccessMethodEnum
  property_count: 0
  slug: posthog-accessmethodenum
- name: Action
  property_count: 19
  slug: posthog-action
- name: ActionConversionGoal
  property_count: 1
  slug: posthog-actionconversiongoal
- name: ActionEnum
  property_count: 0
  slug: posthog-actionenum
- name: ActionReference
  property_count: 6
  slug: posthog-actionreference
- name: ActionsNode
  property_count: 16
  slug: posthog-actionsnode
- name: ActionsPie
  property_count: 2
  slug: posthog-actionspie
- name: ActionStepJSON
  property_count: 11
  slug: posthog-actionstepjson
- name: ActionStepMatchingEnum
  property_count: 0
  slug: posthog-actionstepmatchingenum
- name: ActionStepPropertyFilter
  property_count: 0
  slug: posthog-actionsteppropertyfilter
- name: ActiveBreakpoint
  property_count: 6
  slug: posthog-activebreakpoint
- name: ActiveBreakpointsResponse
  property_count: 1
  slug: posthog-activebreakpointsresponse
- name: ActivityLog
  property_count: 12
  slug: posthog-activitylog
- name: ActivityLogEntry
  property_count: 7
  slug: posthog-activitylogentry
- name: ActivityLogPaginatedResponse
  property_count: 4
  slug: posthog-activitylogpaginatedresponse
- name: ActorsPropertyTaxonomyQuery
  property_count: 8
  slug: posthog-actorspropertytaxonomyquery
- name: ActorsPropertyTaxonomyQueryResponse
  property_count: 7
  slug: posthog-actorspropertytaxonomyqueryresponse
- name: ActorsPropertyTaxonomyResponse
  property_count: 2
  slug: posthog-actorspropertytaxonomyresponse
- name: ActorsQuery
  property_count: 13
  slug: posthog-actorsquery
- name: ActorsQueryResponse
  property_count: 13
  slug: posthog-actorsqueryresponse
- name: AddSnapshotsInput
  property_count: 2
  slug: posthog-addsnapshotsinput
- name: AddSnapshotsResult
  property_count: 2
  slug: posthog-addsnapshotsresult
- name: AgentModeEnum
  property_count: 0
  slug: posthog-agentmodeenum
- name: AggregationAxisFormat
  property_count: 0
  slug: posthog-aggregationaxisformat
- name: AggregationPropertyType
  property_count: 0
  slug: posthog-aggregationpropertytype
- name: AggregationType
  property_count: 0
  slug: posthog-aggregationtype
- name: AIEventType
  property_count: 0
  slug: posthog-aieventtype
- name: Alert
  property_count: 25
  slug: posthog-alert
- name: AlertCheck
  property_count: 16
  slug: posthog-alertcheck
- name: AlertCheckStateEnum
  property_count: 0
  slug: posthog-alertcheckstateenum
- name: AlertCondition
  property_count: 1
  slug: posthog-alertcondition
- name: AlertConditionType
  property_count: 0
  slug: posthog-alertconditiontype
- name: AlertScheduleRestriction
  property_count: 1
  slug: posthog-alertschedulerestriction
- name: AlertScheduleRestrictionWindow
  property_count: 2
  slug: posthog-alertschedulerestrictionwindow
- name: AlertSimulate
  property_count: 4
  slug: posthog-alertsimulate
- name: AlertSimulateResponse
  property_count: 10
  slug: posthog-alertsimulateresponse
- name: Annotation
  property_count: 15
  slug: posthog-annotation
- name: AnnotationScopeEnum
  property_count: 0
  slug: posthog-annotationscopeenum
- name: AppendSegments
  property_count: 1
  slug: posthog-appendsegments
- name: AppMetricSeries
  property_count: 2
  slug: posthog-appmetricseries
- name: AppMetricsResponse
  property_count: 2
  slug: posthog-appmetricsresponse
- name: AppMetricsTotalsResponse
  property_count: 1
  slug: posthog-appmetricstotalsresponse
- name: ApprovalPolicy
  property_count: 12
  slug: posthog-approvalpolicy
- name: ApproveRunRequestInput
  property_count: 3
  slug: posthog-approverunrequestinput
- name: ApproveSnapshotInput
  property_count: 2
  slug: posthog-approvesnapshotinput
- name: ArrayPropertyFilter
  property_count: 4
  slug: posthog-arraypropertyfilter
- name: ArrayPropertyFilterOperatorEnum
  property_count: 0
  slug: posthog-arraypropertyfilteroperatorenum
- name: Artifact
  property_count: 5
  slug: posthog-artifact
- name: AssigneeTypeEnum
  property_count: 0
  slug: posthog-assigneetypeenum
- name: AsyncDeletionStatus
  property_count: 4
  slug: posthog-asyncdeletionstatus
- name: AttributionModeEnum
  property_count: 0
  slug: posthog-attributionmodeenum
- name: AutoApproveResult
  property_count: 2
  slug: posthog-autoapproveresult
- name: AutocompleteCompletionItem
  property_count: 5
  slug: posthog-autocompletecompletionitem
- name: AutocompleteCompletionItemKind
  property_count: 0
  slug: posthog-autocompletecompletionitemkind
- name: AutostartPriorityEnum
  property_count: 0
  slug: posthog-autostartpriorityenum
- name: AvailableFiltersResponse
  property_count: 2
  slug: posthog-availablefiltersresponse
- name: AvailableSetupTaskIdsEnum
  property_count: 0
  slug: posthog-availablesetuptaskidsenum
- name: BaseCurrencyEnum
  property_count: 0
  slug: posthog-basecurrencyenum
- name: BaselineEntry
  property_count: 12
  slug: posthog-baselineentry
- name: BaselineOverview
  property_count: 4
  slug: posthog-baselineoverview
- name: BaselineSparklineDay
  property_count: 4
  slug: posthog-baselinesparklineday
- name: BaselineTotals
  property_count: 5
  slug: posthog-baselinetotals
- name: BaseMathType
  property_count: 0
  slug: posthog-basemathtype
- name: BatchCheckRequest
  property_count: 3
  slug: posthog-batchcheckrequest
- name: BatchCheckResponse
  property_count: 1
  slug: posthog-batchcheckresponse
- name: BatchExport
  property_count: 19
  slug: posthog-batchexport
- name: BatchExportBackfill
  property_count: 12
  slug: posthog-batchexportbackfill
- name: BatchExportBackfillStatusEnum
  property_count: 0
  slug: posthog-batchexportbackfillstatusenum
- name: BatchExportDestination
  property_count: 4
  slug: posthog-batchexportdestination
- name: BatchExportDestinationTypeEnum
  property_count: 0
  slug: posthog-batchexportdestinationtypeenum
- name: BatchExportRun
  property_count: 15
  slug: posthog-batchexportrun
- name: BatchExportRunStatusEnum
  property_count: 0
  slug: posthog-batchexportrunstatusenum
- name: BehavioralFilter
  property_count: 21
  slug: posthog-behavioralfilter
- name: BiasRisk
  property_count: 1
  slug: posthog-biasrisk
- name: BlankEnum
  property_count: 0
  slug: posthog-blankenum
- name: BlastRadius
  property_count: 2
  slug: posthog-blastradius
- name: BlastRadiusRequest
  property_count: 2
  slug: posthog-blastradiusrequest
- name: BooleanScoreDefinitionConfig
  property_count: 2
  slug: posthog-booleanscoredefinitionconfig
- name: BounceRatePageViewMode
  property_count: 0
  slug: posthog-bounceratepageviewmode
- name: BoxPlotDatum
  property_count: 10
  slug: posthog-boxplotdatum
- name: Breakdown
  property_count: 5
  slug: posthog-breakdown
- name: BreakdownAttributionType
  property_count: 0
  slug: posthog-breakdownattributiontype
- name: BreakdownFilter
  property_count: 9
  slug: posthog-breakdownfilter
- name: BreakdownItem
  property_count: 2
  slug: posthog-breakdownitem
- name: BreakdownSimulationResult
  property_count: 9
  slug: posthog-breakdownsimulationresult
- name: BreakdownType
  property_count: 0
  slug: posthog-breakdowntype
- name: BreakdownValue
  property_count: 2
  slug: posthog-breakdownvalue
- name: BreakpointHit
  property_count: 8
  slug: posthog-breakpointhit
- name: BreakpointHitsResponse
  property_count: 3
  slug: posthog-breakpointhitsresponse
- name: BucketingIdentifierEnum
  property_count: 0
  slug: posthog-bucketingidentifierenum
- name: BulkUpdateTagsError
  property_count: 2
  slug: posthog-bulkupdatetagserror
- name: BulkUpdateTagsItem
  property_count: 2
  slug: posthog-bulkupdatetagsitem
- name: BulkUpdateTagsRequest
  property_count: 3
  slug: posthog-bulkupdatetagsrequest
- name: BulkUpdateTagsResponse
  property_count: 2
  slug: posthog-bulkupdatetagsresponse
- name: BusinessModelEnum
  property_count: 0
  slug: posthog-businessmodelenum
- name: ByweekdayEnum
  property_count: 0
  slug: posthog-byweekdayenum
- name: CachedSummary
  property_count: 3
  slug: posthog-cachedsummary
- name: CalculationIntervalEnum
  property_count: 0
  slug: posthog-calculationintervalenum
- name: CalendarHeatmapFilter
  property_count: 1
  slug: posthog-calendarheatmapfilter
- name: CalendarHeatmapMathType
  property_count: 0
  slug: posthog-calendarheatmapmathtype
- name: CalendarHeatmapQuery
  property_count: 15
  slug: posthog-calendarheatmapquery
- name: CalendarHeatmapResponse
  property_count: 8
  slug: posthog-calendarheatmapresponse
- name: CapabilityState
  property_count: 4
  slug: posthog-capabilitystate
- name: CapabilityStateStateEnum
  property_count: 0
  slug: posthog-capabilitystatestateenum
- name: CategoricalScoreDefinitionConfig
  property_count: 4
  slug: posthog-categoricalscoredefinitionconfig
- name: CategoricalScoreOption
  property_count: 2
  slug: posthog-categoricalscoreoption
- name: CategoryEnum
  property_count: 0
  slug: posthog-categoryenum
- name: CdcTableModeEnum
  property_count: 0
  slug: posthog-cdctablemodeenum
- name: Change
  property_count: 5
  slug: posthog-change
- name: ChangeRequest
  property_count: 25
  slug: posthog-changerequest
- name: ChangeRequestStateEnum
  property_count: 0
  slug: posthog-changerequeststateenum
- name: ChannelDetailEnum
  property_count: 0
  slug: posthog-channeldetailenum
- name: ChannelSourceEnum
  property_count: 0
  slug: posthog-channelsourceenum
- name: ChartAxis
  property_count: 2
  slug: posthog-chartaxis
- name: ChartDisplayType
  property_count: 0
  slug: posthog-chartdisplaytype
- name: ChartSettings
  property_count: 17
  slug: posthog-chartsettings
- name: ChartSettingsDisplay
  property_count: 5
  slug: posthog-chartsettingsdisplay
- name: ChartSettingsFormatting
  property_count: 4
  slug: posthog-chartsettingsformatting
- name: CheckDatabaseNameResponse
  property_count: 2
  slug: posthog-checkdatabasenameresponse
- name: ClaudeRuntimeAdapterEnum
  property_count: 0
  slug: posthog-clauderuntimeadapterenum
- name: ClaudeTaskRunCreateSchema
  property_count: 14
  slug: posthog-claudetaskruncreateschema
- name: ClaudeTaskRunCreateSchemaInitialPermissionModeEnum
  property_count: 0
  slug: posthog-claudetaskruncreateschemainitialpermissionmodeenum
- name: ClickhouseEvent
  property_count: 8
  slug: posthog-clickhouseevent
- name: ClickhouseQueryProgress
  property_count: 5
  slug: posthog-clickhousequeryprogress
- name: ClusteringJob
  property_count: 7
  slug: posthog-clusteringjob
- name: ClusteringJobAnalysisLevelEnum
  property_count: 0
  slug: posthog-clusteringjobanalysislevelenum
- name: CodeInviteRedeemRequest
  property_count: 1
  slug: posthog-codeinviteredeemrequest
- name: CodexRuntimeAdapterEnum
  property_count: 0
  slug: posthog-codexruntimeadapterenum
- name: CodexTaskRunCreateSchema
  property_count: 14
  slug: posthog-codextaskruncreateschema
- name: CodexTaskRunCreateSchemaInitialPermissionModeEnum
  property_count: 0
  slug: posthog-codextaskruncreateschemainitialpermissionmodeenum
- name: Cohort
  property_count: 22
  slug: posthog-cohort
- name: CohortFilter
  property_count: 7
  slug: posthog-cohortfilter
- name: CohortFilterGroup
  property_count: 2
  slug: posthog-cohortfiltergroup
- name: CohortFilters
  property_count: 1
  slug: posthog-cohortfilters
- name: CohortPersonResult
  property_count: 11
  slug: posthog-cohortpersonresult
- name: CohortPersonResultTypeEnum
  property_count: 0
  slug: posthog-cohortpersonresulttypeenum
- name: CohortPersonsResponse
  property_count: 3
  slug: posthog-cohortpersonsresponse
- name: CohortPropertyFilter
  property_count: 6
  slug: posthog-cohortpropertyfilter
- name: CohortTypeEnum
  property_count: 0
  slug: posthog-cohorttypeenum
- name: ColorMode
  property_count: 0
  slug: posthog-colormode
- name: Comment
  property_count: 13
  slug: posthog-comment
- name: Compare
  property_count: 0
  slug: posthog-compare
- name: CompareFilter
  property_count: 2
  slug: posthog-comparefilter
- name: CompareItem
  property_count: 2
  slug: posthog-compareitem
- name: ConclusionEnum
  property_count: 0
  slug: posthog-conclusionenum
- name: ConditionalFormattingRule
  property_count: 7
  slug: posthog-conditionalformattingrule
- name: ConnectionTokenResponse
  property_count: 1
  slug: posthog-connectiontokenresponse
- name: ContentEncodingEnum
  property_count: 0
  slug: posthog-contentencodingenum
- name: Conversation
  property_count: 15
  slug: posthog-conversation
- name: ConversationMinimal
  property_count: 10
  slug: posthog-conversationminimal
- name: ConversationStatus
  property_count: 0
  slug: posthog-conversationstatus
- name: ConversationType
  property_count: 0
  slug: posthog-conversationtype
- name: ConversionGoalFilter1
  property_count: 21
  slug: posthog-conversiongoalfilter1
- name: ConversionGoalFilter2
  property_count: 19
  slug: posthog-conversiongoalfilter2
- name: ConversionGoalFilter3
  property_count: 24
  slug: posthog-conversiongoalfilter3
- name: CookielessServerHashModeEnum
  property_count: 0
  slug: posthog-cookielessserverhashmodeenum
- name: COPODDetectorConfig
  property_count: 4
  slug: posthog-copoddetectorconfig
- name: CopyDashboardTemplate
  property_count: 1
  slug: posthog-copydashboardtemplate
- name: CopyDashboardTileRequest
  property_count: 2
  slug: posthog-copydashboardtilerequest
- name: CopyExperimentToProject
  property_count: 3
  slug: posthog-copyexperimenttoproject
- name: CorrelationType
  property_count: 0
  slug: posthog-correlationtype
- name: CountPerActorMathType
  property_count: 0
  slug: posthog-countperactormathtype
- name: CreatedViaEnum
  property_count: 0
  slug: posthog-createdviaenum
- name: CreateGroup
  property_count: 3
  slug: posthog-creategroup
- name: CreateLegalDocument
  property_count: 4
  slug: posthog-createlegaldocument
- name: CreateRecordingRequest
  property_count: 1
  slug: posthog-createrecordingrequest
- name: CreateRecordingRequestPlatformEnum
  property_count: 0
  slug: posthog-createrecordingrequestplatformenum
- name: CreateRecordingResponse
  property_count: 26
  slug: posthog-createrecordingresponse
- name: CreateRepoInput
  property_count: 2
  slug: posthog-createrepoinput
- name: CreateRunInput
  property_count: 11
  slug: posthog-createruninput
- name: CreateRunResult
  property_count: 2
  slug: posthog-createrunresult
- name: CreationModeEnum
  property_count: 0
  slug: posthog-creationmodeenum
- name: CreationTypeEnum
  property_count: 0
  slug: posthog-creationtypeenum
- name: Credential
  property_count: 5
  slug: posthog-credential
- name: CurrencyCode
  property_count: 0
  slug: posthog-currencycode
- name: CustomChannelCondition
  property_count: 4
  slug: posthog-customchannelcondition
- name: CustomChannelField
  property_count: 0
  slug: posthog-customchannelfield
- name: CustomChannelOperator
  property_count: 0
  slug: posthog-customchanneloperator
- name: CustomChannelRule
  property_count: 4
  slug: posthog-customchannelrule
- name: CustomerJourney
  property_count: 7
  slug: posthog-customerjourney
- name: CustomerProfileConfig
  property_count: 6
  slug: posthog-customerprofileconfig
- name: CustomerProfileConfigScopeEnum
  property_count: 0
  slug: posthog-customerprofileconfigscopeenum
- name: CustomEventConversionGoal
  property_count: 1
  slug: posthog-customeventconversiongoal
- name: Dashboard
  property_count: 31
  slug: posthog-dashboard
- name: DashboardBasic
  property_count: 19
  slug: posthog-dashboardbasic
- name: DashboardCollaborator
  property_count: 7
  slug: posthog-dashboardcollaborator
- name: DashboardFilter
  property_count: 5
  slug: posthog-dashboardfilter
- name: DashboardTemplate
  property_count: 15
  slug: posthog-dashboardtemplate
- name: DashboardTemplateScopeEnum
  property_count: 0
  slug: posthog-dashboardtemplatescopeenum
- name: DashboardTileBasic
  property_count: 3
  slug: posthog-dashboardtilebasic
- name: DashboardTileResult
  property_count: 2
  slug: posthog-dashboardtileresult
- name: DatabaseSchemaBatchExportTable
  property_count: 5
  slug: posthog-databaseschemabatchexporttable
- name: DatabaseSchemaDataWarehouseTable
  property_count: 9
  slug: posthog-databaseschemadatawarehousetable
- name: DatabaseSchemaEndpointTable
  property_count: 7
  slug: posthog-databaseschemaendpointtable
- name: DatabaseSchemaField
  property_count: 8
  slug: posthog-databaseschemafield
- name: DatabaseSchemaManagedViewTable
  property_count: 8
  slug: posthog-databaseschemamanagedviewtable
- name: DatabaseSchemaManagedViewTableKind
  property_count: 0
  slug: posthog-databaseschemamanagedviewtablekind
- name: DatabaseSchemaMaterializedViewTable
  property_count: 8
  slug: posthog-databaseschemamaterializedviewtable
- name: DatabaseSchemaPostHogTable
  property_count: 5
  slug: posthog-databaseschemaposthogtable
- name: DatabaseSchemaQuery
  property_count: 6
  slug: posthog-databaseschemaquery
- name: DatabaseSchemaQueryResponse
  property_count: 2
  slug: posthog-databaseschemaqueryresponse
- name: DatabaseSchemaRequest
  property_count: 1
  slug: posthog-databaseschemarequest
- name: DatabaseSchemaSchema
  property_count: 6
  slug: posthog-databaseschemaschema
- name: DatabaseSchemaSource
  property_count: 6
  slug: posthog-databaseschemasource
- name: DatabaseSchemaSystemTable
  property_count: 5
  slug: posthog-databaseschemasystemtable
- name: DatabaseSchemaViewTable
  property_count: 6
  slug: posthog-databaseschemaviewtable
- name: DatabaseSerializedFieldType
  property_count: 0
  slug: posthog-databaseserializedfieldtype
- name: DataColorTheme
  property_count: 6
  slug: posthog-datacolortheme
- name: DataColorToken
  property_count: 0
  slug: posthog-datacolortoken
- name: DataModelingJob
  property_count: 10
  slug: posthog-datamodelingjob
- name: DataModelingJobStatusEnum
  property_count: 0
  slug: posthog-datamodelingjobstatusenum
- name: Dataset
  property_count: 9
  slug: posthog-dataset
- name: DatasetItem
  property_count: 13
  slug: posthog-datasetitem
- name: DataTableNode
  property_count: 38
  slug: posthog-datatablenode
- name: DataTableNodeViewPropsContext
  property_count: 2
  slug: posthog-datatablenodeviewpropscontext
- name: DataTableNodeViewPropsContextType
  property_count: 0
  slug: posthog-datatablenodeviewpropscontexttype
- name: DataVisualizationNode
  property_count: 6
  slug: posthog-datavisualizationnode
- name: DataWarehouseEventsModifier
  property_count: 4
  slug: posthog-datawarehouseeventsmodifier
- name: DataWarehouseModelPath
  property_count: 8
  slug: posthog-datawarehousemodelpath
- name: DataWarehouseNode
  property_count: 21
  slug: posthog-datawarehousenode
- name: DataWarehousePersonPropertyFilter
  property_count: 5
  slug: posthog-datawarehousepersonpropertyfilter
- name: DataWarehousePropertyFilter
  property_count: 5
  slug: posthog-datawarehousepropertyfilter
- name: DataWarehouseSavedQuery
  property_count: 23
  slug: posthog-datawarehousesavedquery
- name: DataWarehouseSavedQueryFolder
  property_count: 6
  slug: posthog-datawarehousesavedqueryfolder
- name: DataWarehouseSavedQueryMinimal
  property_count: 18
  slug: posthog-datawarehousesavedqueryminimal
- name: DataWarehouseViewLink
  property_count: 8
  slug: posthog-datawarehouseviewlink
- name: DateOperatorEnum
  property_count: 0
  slug: posthog-dateoperatorenum
- name: DatePropertyFilter
  property_count: 4
  slug: posthog-datepropertyfilter
- name: DateRange
  property_count: 3
  slug: posthog-daterange
- name: DayItem
  property_count: 2
  slug: posthog-dayitem
- name: DefaultExperimentStatsMethodEnum
  property_count: 0
  slug: posthog-defaultexperimentstatsmethodenum
- name: DeliveryStatusEnum
  property_count: 0
  slug: posthog-deliverystatusenum
- name: DependentFlag
  property_count: 3
  slug: posthog-dependentflag
- name: DeprovisionWarehouseResponse
  property_count: 2
  slug: posthog-deprovisionwarehouseresponse
- name: DescriptionContentTypeEnum
  property_count: 0
  slug: posthog-descriptioncontenttypeenum
- name: DesktopRecording
  property_count: 25
  slug: posthog-desktoprecording
- name: DesktopRecordingStatusEnum
  property_count: 0
  slug: posthog-desktoprecordingstatusenum
- name: DesktopRecordingTask
  property_count: 3
  slug: posthog-desktoprecordingtask
- name: Detail
  property_count: 7
  slug: posthog-detail
- name: DetailedResultsAggregationType
  property_count: 0
  slug: posthog-detailedresultsaggregationtype
- name: DetailModeValueEnum
  property_count: 0
  slug: posthog-detailmodevalueenum
- name: DetectorConfig
  property_count: 0
  slug: posthog-detectorconfig
- name: DeviceTypesEnum
  property_count: 0
  slug: posthog-devicetypesenum
- name: DirectionEnum
  property_count: 0
  slug: posthog-directionenum
- name: DisplayType
  property_count: 0
  slug: posthog-displaytype
- name: DistanceFunc
  property_count: 0
  slug: posthog-distancefunc
- name: DocumentSimilarityQuery
  property_count: 17
  slug: posthog-documentsimilarityquery
- name: DocumentSimilarityQueryResponse
  property_count: 10
  slug: posthog-documentsimilarityqueryresponse
- name: DocumentTypeEnum
  property_count: 0
  slug: posthog-documenttypeenum
- name: DraftStatusResponse
  property_count: 2
  slug: posthog-draftstatusresponse
- name: DurationMetric
  property_count: 3
  slug: posthog-durationmetric
- name: DurationType
  property_count: 0
  slug: posthog-durationtype
- name: EarlyAccessFeature
  property_count: 8
  slug: posthog-earlyaccessfeature
- name: EarlyAccessFeatureSerializerCreateOnly
  property_count: 10
  slug: posthog-earlyaccessfeatureserializercreateonly
- name: ECODDetectorConfig
  property_count: 4
  slug: posthog-ecoddetectorconfig
- name: EffectiveMembershipLevelEnum
  property_count: 0
  slug: posthog-effectivemembershiplevelenum
- name: EffectivePrivilegeLevelEnum
  property_count: 0
  slug: posthog-effectiveprivilegelevelenum
- name: Element
  property_count: 9
  slug: posthog-element
- name: ElementPropertyFilter
  property_count: 5
  slug: posthog-elementpropertyfilter
- name: ElementType
  property_count: 9
  slug: posthog-elementtype
- name: EmbeddedDocument
  property_count: 4
  slug: posthog-embeddeddocument
- name: EmbeddingDistance
  property_count: 3
  slug: posthog-embeddingdistance
- name: EmbeddingModelName
  property_count: 0
  slug: posthog-embeddingmodelname
- name: EmbeddingRecord
  property_count: 6
  slug: posthog-embeddingrecord
- name: EmptyPropertyFilter
  property_count: 1
  slug: posthog-emptypropertyfilter
- name: EndExperiment
  property_count: 2
  slug: posthog-endexperiment
- name: EndpointColumn
  property_count: 2
  slug: posthog-endpointcolumn
- name: EndpointLastExecutionTimesRequest
  property_count: 1
  slug: posthog-endpointlastexecutiontimesrequest
- name: EndpointMaterialization
  property_count: 7
  slug: posthog-endpointmaterialization
- name: EndpointRefreshMode
  property_count: 0
  slug: posthog-endpointrefreshmode
- name: EndpointRequest
  property_count: 10
  slug: posthog-endpointrequest
- name: EndpointResponse
  property_count: 21
  slug: posthog-endpointresponse
- name: EndpointRunRequest
  property_count: 8
  slug: posthog-endpointrunrequest
- name: EndpointRunResponse
  property_count: 5
  slug: posthog-endpointrunresponse
- name: EndpointsUsageBreakdown
  property_count: 0
  slug: posthog-endpointsusagebreakdown
- name: EndpointsUsageOrderByDirection
  property_count: 0
  slug: posthog-endpointsusageorderbydirection
- name: EndpointsUsageOrderByField
  property_count: 0
  slug: posthog-endpointsusageorderbyfield
- name: EndpointsUsageOverviewItem
  property_count: 4
  slug: posthog-endpointsusageoverviewitem
- name: EndpointsUsageOverviewItemKey
  property_count: 0
  slug: posthog-endpointsusageoverviewitemkey
- name: EndpointsUsageOverviewQuery
  property_count: 9
  slug: posthog-endpointsusageoverviewquery
- name: EndpointsUsageOverviewQueryResponse
  property_count: 7
  slug: posthog-endpointsusageoverviewqueryresponse
- name: EndpointsUsageTableQuery
  property_count: 12
  slug: posthog-endpointsusagetablequery
- name: EndpointsUsageTableQueryResponse
  property_count: 12
  slug: posthog-endpointsusagetablequeryresponse
- name: EndpointsUsageTrendsQuery
  property_count: 12
  slug: posthog-endpointsusagetrendsquery
- name: EndpointsUsageTrendsQueryResponse
  property_count: 7
  slug: posthog-endpointsusagetrendsqueryresponse
- name: EndpointVersionResponse
  property_count: 27
  slug: posthog-endpointversionresponse
- name: EnforcementModeEnum
  property_count: 0
  slug: posthog-enforcementmodeenum
- name: EngineEnum
  property_count: 0
  slug: posthog-engineenum
- name: EnsembleDetectorConfig
  property_count: 3
  slug: posthog-ensembledetectorconfig
- name: EnsembleOperator
  property_count: 0
  slug: posthog-ensembleoperator
- name: EnterpriseEventDefinition
  property_count: 24
  slug: posthog-enterpriseeventdefinition
- name: EnterprisePropertyDefinition
  property_count: 13
  slug: posthog-enterprisepropertydefinition
- name: EntityType
  property_count: 0
  slug: posthog-entitytype
- name: ErrorResponse
  property_count: 1
  slug: posthog-errorresponse
- name: ErrorTrackingAssignmentRule
  property_count: 7
  slug: posthog-errortrackingassignmentrule
- name: ErrorTrackingAssignmentRuleAssigneeRequest
  property_count: 2
  slug: posthog-errortrackingassignmentruleassigneerequest
- name: ErrorTrackingAssignmentRuleCreateRequest
  property_count: 2
  slug: posthog-errortrackingassignmentrulecreaterequest
- name: ErrorTrackingAssignmentRuleUpdateRequest
  property_count: 2
  slug: posthog-errortrackingassignmentruleupdaterequest
- name: ErrorTrackingBreakdownsQuery
  property_count: 10
  slug: posthog-errortrackingbreakdownsquery
- name: ErrorTrackingBreakdownsQueryResponse
  property_count: 7
  slug: posthog-errortrackingbreakdownsqueryresponse
- name: ErrorTrackingCorrelatedIssue
  property_count: 13
  slug: posthog-errortrackingcorrelatedissue
- name: ErrorTrackingExternalReference
  property_count: 3
  slug: posthog-errortrackingexternalreference
- name: ErrorTrackingExternalReferenceIntegration
  property_count: 3
  slug: posthog-errortrackingexternalreferenceintegration
- name: ErrorTrackingExternalReferenceIntegrationResult
  property_count: 3
  slug: posthog-errortrackingexternalreferenceintegrationresult
- name: ErrorTrackingExternalReferenceResult
  property_count: 6
  slug: posthog-errortrackingexternalreferenceresult
- name: ErrorTrackingFingerprint
  property_count: 4
  slug: posthog-errortrackingfingerprint
- name: ErrorTrackingGroupingRule
  property_count: 9
  slug: posthog-errortrackinggroupingrule
- name: ErrorTrackingGroupingRuleAssigneeRequest
  property_count: 2
  slug: posthog-errortrackinggroupingruleassigneerequest
- name: ErrorTrackingGroupingRuleCreateRequest
  property_count: 3
  slug: posthog-errortrackinggroupingrulecreaterequest
- name: ErrorTrackingGroupingRuleListResponse
  property_count: 1
  slug: posthog-errortrackinggroupingrulelistresponse
- name: ErrorTrackingIssue
  property_count: 15
  slug: posthog-errortrackingissue
- name: ErrorTrackingIssueAggregations
  property_count: 5
  slug: posthog-errortrackingissueaggregations
- name: ErrorTrackingIssueAssignee
  property_count: 2
  slug: posthog-errortrackingissueassignee
- name: ErrorTrackingIssueAssigneeType
  property_count: 0
  slug: posthog-errortrackingissueassigneetype
- name: ErrorTrackingIssueAssignment
  property_count: 2
  slug: posthog-errortrackingissueassignment
- name: ErrorTrackingIssueCohort
  property_count: 2
  slug: posthog-errortrackingissuecohort
- name: ErrorTrackingIssueCorrelationQuery
  property_count: 6
  slug: posthog-errortrackingissuecorrelationquery
- name: ErrorTrackingIssueCorrelationQueryResponse
  property_count: 11
  slug: posthog-errortrackingissuecorrelationqueryresponse
- name: ErrorTrackingIssueFilter
  property_count: 5
  slug: posthog-errortrackingissuefilter
- name: ErrorTrackingIssueFull
  property_count: 8
  slug: posthog-errortrackingissuefull
- name: ErrorTrackingIssueFullStatusEnum
  property_count: 0
  slug: posthog-errortrackingissuefullstatusenum
- name: ErrorTrackingIssueMergeRequest
  property_count: 1
  slug: posthog-errortrackingissuemergerequest
- name: ErrorTrackingIssueMergeResponse
  property_count: 1
  slug: posthog-errortrackingissuemergeresponse
- name: ErrorTrackingIssueSplitFingerprint
  property_count: 3
  slug: posthog-errortrackingissuesplitfingerprint
- name: ErrorTrackingIssueSplitRequest
  property_count: 1
  slug: posthog-errortrackingissuesplitrequest
- name: ErrorTrackingIssueSplitResponse
  property_count: 2
  slug: posthog-errortrackingissuesplitresponse
- name: ErrorTrackingIssueStatus
  property_count: 0
  slug: posthog-errortrackingissuestatus
- name: ErrorTrackingOrderBy
  property_count: 0
  slug: posthog-errortrackingorderby
- name: ErrorTrackingPendingFingerprintIssueStateUpdate
  property_count: 10
  slug: posthog-errortrackingpendingfingerprintissuestateupdate
- name: ErrorTrackingQuery
  property_count: 26
  slug: posthog-errortrackingquery
- name: ErrorTrackingQueryResponse
  property_count: 11
  slug: posthog-errortrackingqueryresponse
- name: ErrorTrackingRecommendation
  property_count: 8
  slug: posthog-errortrackingrecommendation
- name: ErrorTrackingRelease
  property_count: 7
  slug: posthog-errortrackingrelease
- name: ErrorTrackingSimilarIssuesQuery
  property_count: 12
  slug: posthog-errortrackingsimilarissuesquery
- name: ErrorTrackingSimilarIssuesQueryResponse
  property_count: 10
  slug: posthog-errortrackingsimilarissuesqueryresponse
- name: ErrorTrackingSpikeDetectionConfig
  property_count: 3
  slug: posthog-errortrackingspikedetectionconfig
- name: ErrorTrackingSpikeEvent
  property_count: 5
  slug: posthog-errortrackingspikeevent
- name: ErrorTrackingSpikeEventIssue
  property_count: 3
  slug: posthog-errortrackingspikeeventissue
- name: ErrorTrackingStackFrame
  property_count: 8
  slug: posthog-errortrackingstackframe
- name: ErrorTrackingSuppressionRule
  property_count: 7
  slug: posthog-errortrackingsuppressionrule
- name: ErrorTrackingSuppressionRuleCreateRequest
  property_count: 2
  slug: posthog-errortrackingsuppressionrulecreaterequest
- name: ErrorTrackingSymbolSet
  property_count: 8
  slug: posthog-errortrackingsymbolset
- name: Evaluation
  property_count: 16
  slug: posthog-evaluation
- name: EvaluationConfig
  property_count: 6
  slug: posthog-evaluationconfig
- name: EvaluationConfigSetActiveKeyRequest
  property_count: 1
  slug: posthog-evaluationconfigsetactivekeyrequest
- name: EvaluationPattern
  property_count: 4
  slug: posthog-evaluationpattern
- name: EvaluationReport
  property_count: 18
  slug: posthog-evaluationreport
- name: EvaluationReportFrequencyEnum
  property_count: 0
  slug: posthog-evaluationreportfrequencyenum
- name: EvaluationReportRun
  property_count: 9
  slug: posthog-evaluationreportrun
- name: EvaluationRunRequest
  property_count: 5
  slug: posthog-evaluationrunrequest
- name: EvaluationRuntimeEnum
  property_count: 0
  slug: posthog-evaluationruntimeenum
- name: EvaluationStatusEnum
  property_count: 0
  slug: posthog-evaluationstatusenum
- name: EvaluationSummaryRequest
  property_count: 4
  slug: posthog-evaluationsummaryrequest
- name: EvaluationSummaryResponse
  property_count: 6
  slug: posthog-evaluationsummaryresponse
- name: EvaluationSummaryStatistics
  property_count: 4
  slug: posthog-evaluationsummarystatistics
- name: EvaluationTypeEnum
  property_count: 0
  slug: posthog-evaluationtypeenum
- name: EventDefinition
  property_count: 3
  slug: posthog-eventdefinition
- name: EventDefinitionBasic
  property_count: 2
  slug: posthog-eventdefinitionbasic
- name: EventDefinitionRecord
  property_count: 14
  slug: posthog-eventdefinitionrecord
- name: EventElement
  property_count: 10
  slug: posthog-eventelement
- name: EventFilterConfig
  property_count: 6
  slug: posthog-eventfilterconfig
- name: EventFilterConfigModeEnum
  property_count: 0
  slug: posthog-eventfilterconfigmodeenum
- name: EventMetadataPropertyFilter
  property_count: 5
  slug: posthog-eventmetadatapropertyfilter
- name: EventOddsRatioSerialized
  property_count: 5
  slug: posthog-eventoddsratioserialized
- name: EventPropertyFilter
  property_count: 5
  slug: posthog-eventpropertyfilter
- name: EventPropFilter
  property_count: 4
  slug: posthog-eventpropfilter
- name: EventPropFilterTypeEnum
  property_count: 0
  slug: posthog-eventpropfiltertypeenum
- name: EventSchema
  property_count: 6
  slug: posthog-eventschema
- name: EventsHeatMapColumnAggregationResult
  property_count: 2
  slug: posthog-eventsheatmapcolumnaggregationresult
- name: EventsHeatMapDataResult
  property_count: 3
  slug: posthog-eventsheatmapdataresult
- name: EventsHeatMapRowAggregationResult
  property_count: 2
  slug: posthog-eventsheatmaprowaggregationresult
- name: EventsHeatMapStructuredResult
  property_count: 4
  slug: posthog-eventsheatmapstructuredresult
- name: EventsNode
  property_count: 18
  slug: posthog-eventsnode
- name: EventsQuery
  property_count: 21
  slug: posthog-eventsquery
- name: EventsQueryActionStep
  property_count: 10
  slug: posthog-eventsqueryactionstep
- name: EventsQueryResponse
  property_count: 13
  slug: posthog-eventsqueryresponse
- name: EventTaxonomyItem
  property_count: 3
  slug: posthog-eventtaxonomyitem
- name: EventTaxonomyQuery
  property_count: 11
  slug: posthog-eventtaxonomyquery
- name: EventTaxonomyQueryResponse
  property_count: 10
  slug: posthog-eventtaxonomyqueryresponse
- name: EventType
  property_count: 11
  slug: posthog-eventtype
- name: EventTypeEnum
  property_count: 0
  slug: posthog-eventtypeenum
- name: ExistenceOperatorEnum
  property_count: 0
  slug: posthog-existenceoperatorenum
- name: ExistencePropertyFilter
  property_count: 3
  slug: posthog-existencepropertyfilter
- name: ExitConditionEnum
  property_count: 0
  slug: posthog-exitconditionenum
- name: Experiment
  property_count: 36
  slug: posthog-experiment
- name: ExperimentActorsQuery
  property_count: 12
  slug: posthog-experimentactorsquery
- name: ExperimentApiEventSource
  property_count: 4
  slug: posthog-experimentapieventsource
- name: ExperimentApiExposureConfig
  property_count: 3
  slug: posthog-experimentapiexposureconfig
- name: ExperimentApiExposureCriteria
  property_count: 2
  slug: posthog-experimentapiexposurecriteria
- name: ExperimentApiMetric
  property_count: 16
  slug: posthog-experimentapimetric
- name: _ExperimentApiMetricsList
  property_count: 0
  slug: posthog-experimentapimetricslist
- name: ExperimentBreakdownResult
  property_count: 3
  slug: posthog-experimentbreakdownresult
- name: ExperimentDataWarehouseNode
  property_count: 19
  slug: posthog-experimentdatawarehousenode
- name: ExperimentEventExposureConfig
  property_count: 5
  slug: posthog-experimenteventexposureconfig
- name: ExperimentExposureCriteria
  property_count: 3
  slug: posthog-experimentexposurecriteria
- name: ExperimentExposureQuery
  property_count: 12
  slug: posthog-experimentexposurequery
- name: ExperimentExposureQueryResponse
  property_count: 6
  slug: posthog-experimentexposurequeryresponse
- name: ExperimentExposureTimeSeries
  property_count: 3
  slug: posthog-experimentexposuretimeseries
- name: ExperimentFunnelMetric
  property_count: 15
  slug: posthog-experimentfunnelmetric
- name: ExperimentFunnelsQuery
  property_count: 10
  slug: posthog-experimentfunnelsquery
- name: ExperimentFunnelsQueryResponse
  property_count: 10
  slug: posthog-experimentfunnelsqueryresponse
- name: ExperimentHoldout
  property_count: 7
  slug: posthog-experimentholdout
- name: ExperimentHoldoutType
  property_count: 7
  slug: posthog-experimentholdouttype
- name: ExperimentMeanMetric
  property_count: 17
  slug: posthog-experimentmeanmetric
- name: ExperimentMetricGoal
  property_count: 0
  slug: posthog-experimentmetricgoal
- name: ExperimentMetricKindEnum
  property_count: 0
  slug: posthog-experimentmetrickindenum
- name: ExperimentMetricMathType
  property_count: 0
  slug: posthog-experimentmetricmathtype
- name: ExperimentMetricType
  property_count: 0
  slug: posthog-experimentmetrictype
- name: ExperimentParameters
  property_count: 3
  slug: posthog-experimentparameters
- name: ExperimentQuery
  property_count: 9
  slug: posthog-experimentquery
- name: ExperimentQueryResponse
  property_count: 16
  slug: posthog-experimentqueryresponse
- name: ExperimentRatioMetric
  property_count: 15
  slug: posthog-experimentratiometric
- name: ExperimentRetentionMetric
  property_count: 19
  slug: posthog-experimentretentionmetric
- name: ExperimentSavedMetric
  property_count: 9
  slug: posthog-experimentsavedmetric
- name: ExperimentSignificanceCode
  property_count: 0
  slug: posthog-experimentsignificancecode
- name: ExperimentStatsBaseValidated
  property_count: 13
  slug: posthog-experimentstatsbasevalidated
- name: ExperimentStatsValidationFailure
  property_count: 0
  slug: posthog-experimentstatsvalidationfailure
- name: ExperimentStatusEnum
  property_count: 0
  slug: posthog-experimentstatusenum
- name: ExperimentToSavedMetric
  property_count: 7
  slug: posthog-experimenttosavedmetric
- name: ExperimentTrendsQuery
  property_count: 11
  slug: posthog-experimenttrendsquery
- name: ExperimentTrendsQueryResponse
  property_count: 11
  slug: posthog-experimenttrendsqueryresponse
- name: ExperimentTypeEnum
  property_count: 0
  slug: posthog-experimenttypeenum
- name: ExperimentVariant
  property_count: 4
  slug: posthog-experimentvariant
- name: ExperimentVariantFunnelsBaseStats
  property_count: 3
  slug: posthog-experimentvariantfunnelsbasestats
- name: ExperimentVariantResultBayesian
  property_count: 17
  slug: posthog-experimentvariantresultbayesian
- name: ExperimentVariantResultFrequentist
  property_count: 17
  slug: posthog-experimentvariantresultfrequentist
- name: ExperimentVariantTrendsBaseStats
  property_count: 4
  slug: posthog-experimentvarianttrendsbasestats
- name: ExplainRequest
  property_count: 3
  slug: posthog-explainrequest
- name: ExportedAsset
  property_count: 10
  slug: posthog-exportedasset
- name: ExportFormatEnum
  property_count: 0
  slug: posthog-exportformatenum
- name: ExternalDataSchema
  property_count: 17
  slug: posthog-externaldataschema
- name: ExternalDataSourceBulkUpdateSchema
  property_count: 8
  slug: posthog-externaldatasourcebulkupdateschema
- name: ExternalDataSourceConnectionOption
  property_count: 3
  slug: posthog-externaldatasourceconnectionoption
- name: ExternalDataSourceCreate
  property_count: 6
  slug: posthog-externaldatasourcecreate
- name: ExternalDataSourceRevenueAnalyticsConfig
  property_count: 2
  slug: posthog-externaldatasourcerevenueanalyticsconfig
- name: ExternalDataSourceSerializers
  property_count: 19
  slug: posthog-externaldatasourceserializers
- name: ExternalDataSourceTypeEnum
  property_count: 0
  slug: posthog-externaldatasourcetypeenum
- name: ExternalQueryError
  property_count: 2
  slug: posthog-externalqueryerror
- name: ExternalQueryErrorCode
  property_count: 0
  slug: posthog-externalqueryerrorcode
- name: ExternalQueryStatus
  property_count: 0
  slug: posthog-externalquerystatus
- name: FeatureFlag
  property_count: 35
  slug: posthog-featureflag
- name: FeatureFlagConditionGroupSchema
  property_count: 4
  slug: posthog-featureflagconditiongroupschema
- name: FeatureFlagCreateRequestSchema
  property_count: 6
  slug: posthog-featureflagcreaterequestschema
- name: FeatureFlagCreationContextEnum
  property_count: 0
  slug: posthog-featureflagcreationcontextenum
- name: FeatureFlagFilterPropertyCohortInSchema
  property_count: 6
  slug: posthog-featureflagfilterpropertycohortinschema
- name: FeatureFlagFilterPropertyCohortInSchemaOperatorEnum
  property_count: 0
  slug: posthog-featureflagfilterpropertycohortinschemaoperatorenum
- name: FeatureFlagFilterPropertyCohortInSchemaTypeEnum
  property_count: 0
  slug: posthog-featureflagfilterpropertycohortinschematypeenum
- name: FeatureFlagFilterPropertyDateSchema
  property_count: 6
  slug: posthog-featureflagfilterpropertydateschema
- name: FeatureFlagFilterPropertyExistsSchema
  property_count: 6
  slug: posthog-featureflagfilterpropertyexistsschema
- name: FeatureFlagFilterPropertyFlagEvaluatesSchema
  property_count: 6
  slug: posthog-featureflagfilterpropertyflagevaluatesschema
- name: FeatureFlagFilterPropertyFlagEvaluatesSchemaOperatorEnum
  property_count: 0
  slug: posthog-featureflagfilterpropertyflagevaluatesschemaoperatorenum
- name: FeatureFlagFilterPropertyFlagEvaluatesSchemaTypeEnum
  property_count: 0
  slug: posthog-featureflagfilterpropertyflagevaluatesschematypeenum
- name: FeatureFlagFilterPropertyGenericSchema
  property_count: 6
  slug: posthog-featureflagfilterpropertygenericschema
- name: FeatureFlagFilterPropertyGenericSchemaOperatorEnum
  property_count: 0
  slug: posthog-featureflagfilterpropertygenericschemaoperatorenum
- name: FeatureFlagFilterPropertyMultiContainsSchema
  property_count: 6
  slug: posthog-featureflagfilterpropertymulticontainsschema
- name: FeatureFlagFilterPropertyMultiContainsSchemaOperatorEnum
  property_count: 0
  slug: posthog-featureflagfilterpropertymulticontainsschemaoperatorenum
- name: FeatureFlagFilterPropertySchema
  property_count: 0
  slug: posthog-featureflagfilterpropertyschema
- name: FeatureFlagFilterPropertySemverSchema
  property_count: 6
  slug: posthog-featureflagfilterpropertysemverschema
- name: FeatureFlagFilterPropertySemverSchemaOperatorEnum
  property_count: 0
  slug: posthog-featureflagfilterpropertysemverschemaoperatorenum
- name: FeatureFlagFiltersSchema
  property_count: 6
  slug: posthog-featureflagfiltersschema
- name: FeatureFlagGroupType
  property_count: 7
  slug: posthog-featureflaggrouptype
- name: FeatureFlagMultivariateSchema
  property_count: 1
  slug: posthog-featureflagmultivariateschema
- name: FeatureFlagMultivariateVariantSchema
  property_count: 3
  slug: posthog-featureflagmultivariatevariantschema
- name: FeatureFlagStatusResponse
  property_count: 2
  slug: posthog-featureflagstatusresponse
- name: FeatureFlagVersionResponse
  property_count: 21
  slug: posthog-featureflagversionresponse
- name: FeaturePropertyFilter
  property_count: 5
  slug: posthog-featurepropertyfilter
- name: FileSystem
  property_count: 10
  slug: posthog-filesystem
- name: FileSystemShortcut
  property_count: 7
  slug: posthog-filesystemshortcut
- name: FileSystemShortcutReorder
  property_count: 1
  slug: posthog-filesystemshortcutreorder
- name: FilterEnum
  property_count: 0
  slug: posthog-filterenum
- name: FilterLogicalOperator
  property_count: 0
  slug: posthog-filterlogicaloperator
- name: Filters
  property_count: 2
  slug: posthog-filters
- name: FirstEvent
  property_count: 4
  slug: posthog-firstevent
- name: FlagPropertyFilter
  property_count: 5
  slug: posthog-flagpropertyfilter
- name: FlagValueItem
  property_count: 1
  slug: posthog-flagvalueitem
- name: FlagValueResponse
  property_count: 2
  slug: posthog-flagvalueresponse
- name: FunnelConversionWindowTimeUnit
  property_count: 0
  slug: posthog-funnelconversionwindowtimeunit
- name: FunnelCorrelationActorsQuery
  property_count: 10
  slug: posthog-funnelcorrelationactorsquery
- name: FunnelCorrelationQuery
  property_count: 10
  slug: posthog-funnelcorrelationquery
- name: FunnelCorrelationResponse
  property_count: 12
  slug: posthog-funnelcorrelationresponse
- name: FunnelCorrelationResult
  property_count: 2
  slug: posthog-funnelcorrelationresult
- name: FunnelCorrelationResultsType
  property_count: 0
  slug: posthog-funnelcorrelationresultstype
- name: FunnelExclusionActionsNode
  property_count: 18
  slug: posthog-funnelexclusionactionsnode
- name: FunnelExclusionEventsNode
  property_count: 20
  slug: posthog-funnelexclusioneventsnode
- name: FunnelLayout
  property_count: 0
  slug: posthog-funnellayout
- name: FunnelMathType
  property_count: 0
  slug: posthog-funnelmathtype
- name: FunnelPathsFilter
  property_count: 3
  slug: posthog-funnelpathsfilter
- name: FunnelPathType
  property_count: 0
  slug: posthog-funnelpathtype
- name: FunnelsActorsQuery
  property_count: 11
  slug: posthog-funnelsactorsquery
- name: FunnelsDataWarehouseNode
  property_count: 21
  slug: posthog-funnelsdatawarehousenode
- name: FunnelsFilter
  property_count: 21
  slug: posthog-funnelsfilter
- name: FunnelsQuery
  property_count: 15
  slug: posthog-funnelsquery
- name: FunnelsQueryResponse
  property_count: 7
  slug: posthog-funnelsqueryresponse
- name: FunnelStepReference
  property_count: 0
  slug: posthog-funnelstepreference
- name: FunnelVizType
  property_count: 0
  slug: posthog-funnelviztype
- name: GeneratedSurveyQuestionTranslation
  property_count: 7
  slug: posthog-generatedsurveyquestiontranslation
- name: GeneratedSurveyQuestionTranslationPatch
  property_count: 2
  slug: posthog-generatedsurveyquestiontranslationpatch
- name: GeneratedSurveyRootTranslation
  property_count: 4
  slug: posthog-generatedsurveyroottranslation
- name: GenerateRequest
  property_count: 3
  slug: posthog-generaterequest
- name: GenerateResponse
  property_count: 1
  slug: posthog-generateresponse
- name: GenerateStepResponse
  property_count: 3
  slug: posthog-generatestepresponse
- name: GenerateSurveyTranslationsRequest
  property_count: 4
  slug: posthog-generatesurveytranslationsrequest
- name: GenerateSurveyTranslationsResponse
  property_count: 4
  slug: posthog-generatesurveytranslationsresponse
- name: GitHubBranchesResponse
  property_count: 3
  slug: posthog-githubbranchesresponse
- name: GitHubRepo
  property_count: 3
  slug: posthog-githubrepo
- name: GitHubReposRefreshResponse
  property_count: 1
  slug: posthog-githubreposrefreshresponse
- name: GitHubReposResponse
  property_count: 2
  slug: posthog-githubreposresponse
- name: GitProviderFileLinkResolveResponse
  property_count: 3
  slug: posthog-gitproviderfilelinkresolveresponse
- name: Goal
  property_count: 3
  slug: posthog-goal
- name: GoalLine
  property_count: 6
  slug: posthog-goalline
- name: GradientScaleMode
  property_count: 0
  slug: posthog-gradientscalemode
- name: Group
  property_count: 4
  slug: posthog-group
- name: GroupNode
  property_count: 19
  slug: posthog-groupnode
- name: GroupPropertyFilter
  property_count: 7
  slug: posthog-grouppropertyfilter
- name: GroupsQuery
  property_count: 12
  slug: posthog-groupsquery
- name: GroupsQueryResponse
  property_count: 13
  slug: posthog-groupsqueryresponse
- name: GroupType
  property_count: 7
  slug: posthog-grouptype
- name: GroupUsageMetric
  property_count: 8
  slug: posthog-groupusagemetric
- name: GroupUsageMetricDisplayEnum
  property_count: 0
  slug: posthog-groupusagemetricdisplayenum
- name: GroupUsageMetricFormatEnum
  property_count: 0
  slug: posthog-groupusagemetricformatenum
- name: HBOSDetectorConfig
  property_count: 5
  slug: posthog-hbosdetectorconfig
- name: HealthEnum
  property_count: 0
  slug: posthog-healthenum
- name: HealthIssue
  property_count: 9
  slug: posthog-healthissue
- name: HealthIssueSeverityEnum
  property_count: 0
  slug: posthog-healthissueseverityenum
- name: HealthIssueStatusEnum
  property_count: 0
  slug: posthog-healthissuestatusenum
- name: HeatmapGradientStop
  property_count: 2
  slug: posthog-heatmapgradientstop
- name: HeatmapResponseItem
  property_count: 4
  slug: posthog-heatmapresponseitem
- name: HeatmapScreenshotResponse
  property_count: 15
  slug: posthog-heatmapscreenshotresponse
- name: HeatmapScreenshotResponseStatusEnum
  property_count: 0
  slug: posthog-heatmapscreenshotresponsestatusenum
- name: HeatmapScreenshotResponseTypeEnum
  property_count: 0
  slug: posthog-heatmapscreenshotresponsetypeenum
- name: HeatmapSettings
  property_count: 12
  slug: posthog-heatmapsettings
- name: HeatmapSortOrder
  property_count: 0
  slug: posthog-heatmapsortorder
- name: HeatmapsResponse
  property_count: 1
  slug: posthog-heatmapsresponse
- name: HedgehogActorAccessoryOption
  property_count: 0
  slug: posthog-hedgehogactoraccessoryoption
- name: HedgehogActorColorOption
  property_count: 0
  slug: posthog-hedgehogactorcoloroption
- name: HedgehogActorSkinOption
  property_count: 0
  slug: posthog-hedgehogactorskinoption
- name: HogFlow
  property_count: 17
  slug: posthog-hogflow
- name: HogFlowAction
  property_count: 10
  slug: posthog-hogflowaction
- name: HogFlowMasking
  property_count: 4
  slug: posthog-hogflowmasking
- name: HogFlowMinimal
  property_count: 17
  slug: posthog-hogflowminimal
- name: HogFlowSchedule
  property_count: 9
  slug: posthog-hogflowschedule
- name: HogFlowScheduleStatusEnum
  property_count: 0
  slug: posthog-hogflowschedulestatusenum
- name: HogFlowStatusEnum
  property_count: 0
  slug: posthog-hogflowstatusenum
- name: HogFunction
  property_count: 24
  slug: posthog-hogfunction
- name: HogFunctionFilters
  property_count: 9
  slug: posthog-hogfunctionfilters
- name: HogFunctionFiltersSourceEnum
  property_count: 0
  slug: posthog-hogfunctionfilterssourceenum
- name: HogFunctionInvocation
  property_count: 7
  slug: posthog-hogfunctioninvocation
- name: HogFunctionMappingTemplate
  property_count: 6
  slug: posthog-hogfunctionmappingtemplate
- name: HogFunctionMasking
  property_count: 4
  slug: posthog-hogfunctionmasking
- name: HogFunctionMinimal
  property_count: 14
  slug: posthog-hogfunctionminimal
- name: HogFunctionStatus
  property_count: 2
  slug: posthog-hogfunctionstatus
- name: HogFunctionStatusStateEnum
  property_count: 0
  slug: posthog-hogfunctionstatusstateenum
- name: HogFunctionTemplate
  property_count: 14
  slug: posthog-hogfunctiontemplate
- name: HogFunctionTemplatingEnum
  property_count: 0
  slug: posthog-hogfunctiontemplatingenum
- name: HogFunctionTypeEnum
  property_count: 0
  slug: posthog-hogfunctiontypeenum
- name: HogLanguage
  property_count: 0
  slug: posthog-hoglanguage
- name: HogQLAutocomplete
  property_count: 13
  slug: posthog-hogqlautocomplete
- name: HogQLAutocompleteResponse
  property_count: 3
  slug: posthog-hogqlautocompleteresponse
- name: HogQLFilter
  property_count: 3
  slug: posthog-hogqlfilter
- name: HogQLFilters
  property_count: 3
  slug: posthog-hogqlfilters
- name: HogQLMetadata
  property_count: 13
  slug: posthog-hogqlmetadata
- name: HogQLMetadataResponse
  property_count: 8
  slug: posthog-hogqlmetadataresponse
- name: HogQLNotice
  property_count: 4
  slug: posthog-hogqlnotice
- name: HogQLPropertyFilter
  property_count: 4
  slug: posthog-hogqlpropertyfilter
- name: HogQLQuery
  property_count: 13
  slug: posthog-hogqlquery
- name: HogQLQueryModifiers
  property_count: 27
  slug: posthog-hogqlquerymodifiers
- name: HogQLQueryResponse
  property_count: 16
  slug: posthog-hogqlqueryresponse
- name: HogQLVariable
  property_count: 4
  slug: posthog-hogqlvariable
- name: HogQuery
  property_count: 6
  slug: posthog-hogquery
- name: HogQueryResponse
  property_count: 4
  slug: posthog-hogqueryresponse
- name: HrefMatching
  property_count: 0
  slug: posthog-hrefmatching
- name: InCohortVia
  property_count: 0
  slug: posthog-incohortvia
- name: IncrementalFieldTypeEnum
  property_count: 0
  slug: posthog-incrementalfieldtypeenum
- name: InlineCohortCalculation
  property_count: 0
  slug: posthog-inlinecohortcalculation
- name: InputsItem
  property_count: 5
  slug: posthog-inputsitem
- name: InputsSchemaItem
  property_count: 15
  slug: posthog-inputsschemaitem
- name: InputsSchemaItemTypeEnum
  property_count: 0
  slug: posthog-inputsschemaitemtypeenum
- name: Insight
  property_count: 36
  slug: posthog-insight
- name: InsightActorsQuery
  property_count: 13
  slug: posthog-insightactorsquery
- name: InsightActorsQueryOptions
  property_count: 4
  slug: posthog-insightactorsqueryoptions
- name: InsightActorsQueryOptionsResponse
  property_count: 7
  slug: posthog-insightactorsqueryoptionsresponse
- name: _InsightQuerySchema
  property_count: 0
  slug: posthog-insightqueryschema
- name: InsightResult
  property_count: 5
  slug: posthog-insightresult
- name: InsightsThresholdBounds
  property_count: 2
  slug: posthog-insightsthresholdbounds
- name: InsightsToolCall
  property_count: 2
  slug: posthog-insightstoolcall
- name: InsightThreshold
  property_count: 2
  slug: posthog-insightthreshold
- name: InsightThresholdType
  property_count: 0
  slug: posthog-insightthresholdtype
- name: InsightTypeEnum
  property_count: 0
  slug: posthog-insighttypeenum
- name: InsightVariable
  property_count: 8
  slug: posthog-insightvariable
- name: InsightVariableTypeEnum
  property_count: 0
  slug: posthog-insightvariabletypeenum
- name: InsightVizNode
  property_count: 16
  slug: posthog-insightviznode
- name: InstallCustom
  property_count: 9
  slug: posthog-installcustom
- name: InstallCustomAuthTypeEnum
  property_count: 0
  slug: posthog-installcustomauthtypeenum
- name: InstallSourceEnum
  property_count: 0
  slug: posthog-installsourceenum
- name: InstallTemplate
  property_count: 4
  slug: posthog-installtemplate
- name: Integration
  property_count: 3
  slug: posthog-integration
- name: IntegrationConfig
  property_count: 7
  slug: posthog-integrationconfig
- name: IntegrationFilter
  property_count: 1
  slug: posthog-integrationfilter
- name: IntegrationKind
  property_count: 0
  slug: posthog-integrationkind
- name: IntegrationKindEnum
  property_count: 0
  slug: posthog-integrationkindenum
- name: InterestingNote
  property_count: 2
  slug: posthog-interestingnote
- name: IntervalEnum
  property_count: 0
  slug: posthog-intervalenum
- name: IntervalItem
  property_count: 2
  slug: posthog-intervalitem
- name: IntervalType
  property_count: 0
  slug: posthog-intervaltype
- name: InvestigationInconclusiveActionEnum
  property_count: 0
  slug: posthog-investigationinconclusiveactionenum
- name: InvestigationStatusEnum
  property_count: 0
  slug: posthog-investigationstatusenum
- name: InvestigationVerdictEnum
  property_count: 0
  slug: posthog-investigationverdictenum
- name: IQRDetectorConfig
  property_count: 4
  slug: posthog-iqrdetectorconfig
- name: IsolationForestDetectorConfig
  property_count: 5
  slug: posthog-isolationforestdetectorconfig
- name: JsonrpcEnum
  property_count: 0
  slug: posthog-jsonrpcenum
- name: Key10
  property_count: 0
  slug: posthog-key10
- name: Kind
  property_count: 0
  slug: posthog-kind
- name: KNNDetectorConfig
  property_count: 6
  slug: posthog-knndetectorconfig
- name: LastActiveEnum
  property_count: 0
  slug: posthog-lastactiveenum
- name: LastEvent
  property_count: 4
  slug: posthog-lastevent
- name: LegalDocumentCreator
  property_count: 2
  slug: posthog-legaldocumentcreator
- name: LegalDocumentDTO
  property_count: 7
  slug: posthog-legaldocumentdto
- name: LifecycleDataWarehouseNode
  property_count: 20
  slug: posthog-lifecycledatawarehousenode
- name: LifecycleFilter
  property_count: 4
  slug: posthog-lifecyclefilter
- name: LifecycleQuery
  property_count: 15
  slug: posthog-lifecyclequery
- name: LifecycleQueryResponse
  property_count: 7
  slug: posthog-lifecyclequeryresponse
- name: LifecycleToggle
  property_count: 0
  slug: posthog-lifecycletoggle
- name: LimitContext
  property_count: 0
  slug: posthog-limitcontext
- name: LiveDebuggerBreakpoint
  property_count: 8
  slug: posthog-livedebuggerbreakpoint
- name: LLMModelInfo
  property_count: 2
  slug: posthog-llmmodelinfo
- name: LLMModelsListResponse
  property_count: 1
  slug: posthog-llmmodelslistresponse
- name: LLMPrompt
  property_count: 13
  slug: posthog-llmprompt
- name: LLMPromptDuplicate
  property_count: 1
  slug: posthog-llmpromptduplicate
- name: LLMPromptEditOperation
  property_count: 2
  slug: posthog-llmprompteditoperation
- name: LLMPromptList
  property_count: 15
  slug: posthog-llmpromptlist
- name: LLMPromptOutlineEntry
  property_count: 2
  slug: posthog-llmpromptoutlineentry
- name: LLMPromptPublic
  property_count: 13
  slug: posthog-llmpromptpublic
- name: LLMPromptResolveResponse
  property_count: 3
  slug: posthog-llmpromptresolveresponse
- name: LLMPromptVersionSummary
  property_count: 5
  slug: posthog-llmpromptversionsummary
- name: LLMProviderEnum
  property_count: 0
  slug: posthog-llmproviderenum
- name: LLMProviderKey
  property_count: 15
  slug: posthog-llmproviderkey
- name: LLMProviderKeyStateEnum
  property_count: 0
  slug: posthog-llmproviderkeystateenum
- name: LLMSkill
  property_count: 19
  slug: posthog-llmskill
- name: LLMSkillCreate
  property_count: 19
  slug: posthog-llmskillcreate
- name: LLMSkillDuplicate
  property_count: 1
  slug: posthog-llmskillduplicate
- name: LLMSkillEditOperation
  property_count: 2
  slug: posthog-llmskilleditoperation
- name: LLMSkillFile
  property_count: 3
  slug: posthog-llmskillfile
- name: LLMSkillFileCreate
  property_count: 4
  slug: posthog-llmskillfilecreate
- name: LLMSkillFileEdit
  property_count: 2
  slug: posthog-llmskillfileedit
- name: LLMSkillFileInput
  property_count: 3
  slug: posthog-llmskillfileinput
- name: LLMSkillFileManifest
  property_count: 2
  slug: posthog-llmskillfilemanifest
- name: LLMSkillFileRename
  property_count: 3
  slug: posthog-llmskillfilerename
- name: LLMSkillList
  property_count: 17
  slug: posthog-llmskilllist
- name: LLMSkillOutlineEntry
  property_count: 2
  slug: posthog-llmskilloutlineentry
- name: LLMSkillResolveResponse
  property_count: 3
  slug: posthog-llmskillresolveresponse
- name: LLMSkillVersionSummary
  property_count: 5
  slug: posthog-llmskillversionsummary
- name: LLMTrace
  property_count: 20
  slug: posthog-llmtrace
- name: LLMTraceEvent
  property_count: 4
  slug: posthog-llmtraceevent
- name: LLMTracePerson
  property_count: 4
  slug: posthog-llmtraceperson
- name: LocalEvaluationResponse
  property_count: 3
  slug: posthog-localevaluationresponse
- name: LOFDetectorConfig
  property_count: 5
  slug: posthog-lofdetectorconfig
- name: _LogAttributeEntry
  property_count: 4
  slug: posthog-logattributeentry
- name: LogAttributeResult
  property_count: 4
  slug: posthog-logattributeresult
- name: LogAttributesQuery
  property_count: 14
  slug: posthog-logattributesquery
- name: LogAttributesQueryResponse
  property_count: 8
  slug: posthog-logattributesqueryresponse
- name: _LogAttributeValue
  property_count: 2
  slug: posthog-logattributevalue
- name: _LogEntry
  property_count: 13
  slug: posthog-logentry
- name: LogEntryPropertyFilter
  property_count: 5
  slug: posthog-logentrypropertyfilter
- name: LogPropertyFilter
  property_count: 5
  slug: posthog-logpropertyfilter
- name: _LogPropertyFilterOperatorEnum
  property_count: 0
  slug: posthog-logpropertyfilteroperatorenum
- name: LogPropertyFilterType
  property_count: 0
  slug: posthog-logpropertyfiltertype
- name: _LogPropertyFilterTypeEnum
  property_count: 0
  slug: posthog-logpropertyfiltertypeenum
- name: LogsAlertConfiguration
  property_count: 24
  slug: posthog-logsalertconfiguration
- name: LogsAlertConfigurationStateEnum
  property_count: 0
  slug: posthog-logsalertconfigurationstateenum
- name: LogsAlertCreateDestination
  property_count: 5
  slug: posthog-logsalertcreatedestination
- name: LogsAlertDeleteDestination
  property_count: 1
  slug: posthog-logsalertdeletedestination
- name: LogsAlertDestinationResponse
  property_count: 1
  slug: posthog-logsalertdestinationresponse
- name: LogsAlertEvent
  property_count: 9
  slug: posthog-logsalertevent
- name: LogsAlertEventKindEnum
  property_count: 0
  slug: posthog-logsalerteventkindenum
- name: LogsAlertSimulateBucket
  property_count: 6
  slug: posthog-logsalertsimulatebucket
- name: LogsAlertSimulateRequest
  property_count: 8
  slug: posthog-logsalertsimulaterequest
- name: LogsAlertSimulateResponse
  property_count: 6
  slug: posthog-logsalertsimulateresponse
- name: LogsAlertStateInterval
  property_count: 4
  slug: posthog-logsalertstateinterval
- name: _LogsAttributesResponse
  property_count: 2
  slug: posthog-logsattributesresponse
- name: _LogsCountBody
  property_count: 5
  slug: posthog-logscountbody
- name: _LogsCountRangeBucket
  property_count: 3
  slug: posthog-logscountrangebucket
- name: _LogsCountRangesBody
  property_count: 6
  slug: posthog-logscountrangesbody
- name: _LogsCountRangesRequest
  property_count: 1
  slug: posthog-logscountrangesrequest
- name: _LogsCountRangesResponse
  property_count: 2
  slug: posthog-logscountrangesresponse
- name: _LogsCountRequest
  property_count: 1
  slug: posthog-logscountrequest
- name: _LogsCountResponse
  property_count: 1
  slug: posthog-logscountresponse
- name: LogSeverityLevel
  property_count: 0
  slug: posthog-logseveritylevel
- name: LogsOrderBy
  property_count: 0
  slug: posthog-logsorderby
- name: LogsQuery
  property_count: 17
  slug: posthog-logsquery
- name: _LogsQueryBody
  property_count: 8
  slug: posthog-logsquerybody
- name: _LogsQueryRequest
  property_count: 1
  slug: posthog-logsqueryrequest
- name: LogsQueryResponse
  property_count: 12
  slug: posthog-logsqueryresponse
- name: LogsSamplingRule
  property_count: 13
  slug: posthog-logssamplingrule
- name: LogsSamplingRuleReorder
  property_count: 1
  slug: posthog-logssamplingrulereorder
- name: LogsSamplingRuleSimulateResponse
  property_count: 2
  slug: posthog-logssamplingrulesimulateresponse
- name: _LogsServiceActiveRule
  property_count: 3
  slug: posthog-logsserviceactiverule
- name: _LogsServiceAggregate
  property_count: 7
  slug: posthog-logsserviceaggregate
- name: _LogsServicesBody
  property_count: 5
  slug: posthog-logsservicesbody
- name: _LogsServiceSeverityBreakdown
  property_count: 4
  slug: posthog-logsserviceseveritybreakdown
- name: _LogsServicesRequest
  property_count: 1
  slug: posthog-logsservicesrequest
- name: _LogsServicesResponse
  property_count: 3
  slug: posthog-logsservicesresponse
- name: _LogsServicesSparklineBucket
  property_count: 3
  slug: posthog-logsservicessparklinebucket
- name: _LogsServicesSummary
  property_count: 2
  slug: posthog-logsservicessummary
- name: _LogsSparklineBody
  property_count: 6
  slug: posthog-logssparklinebody
- name: LogsSparklineBreakdownBy
  property_count: 0
  slug: posthog-logssparklinebreakdownby
- name: _LogsSparklineBucket
  property_count: 4
  slug: posthog-logssparklinebucket
- name: _LogsSparklineRequest
  property_count: 1
  slug: posthog-logssparklinerequest
- name: _LogsSparklineResponse
  property_count: 1
  slug: posthog-logssparklineresponse
- name: _LogsValuesResponse
  property_count: 2
  slug: posthog-logsvaluesresponse
- name: LogsView
  property_count: 8
  slug: posthog-logsview
- name: LogValueResult
  property_count: 2
  slug: posthog-logvalueresult
- name: LogValuesQuery
  property_count: 14
  slug: posthog-logvaluesquery
- name: LogValuesQueryResponse
  property_count: 7
  slug: posthog-logvaluesqueryresponse
- name: MADDetectorConfig
  property_count: 4
  slug: posthog-maddetectorconfig
- name: Mappings
  property_count: 4
  slug: posthog-mappings
- name: MarketingAnalyticsAggregatedQuery
  property_count: 22
  slug: posthog-marketinganalyticsaggregatedquery
- name: MarketingAnalyticsAggregatedQueryResponse
  property_count: 8
  slug: posthog-marketinganalyticsaggregatedqueryresponse
- name: MarketingAnalyticsDrillDownLevel
  property_count: 0
  slug: posthog-marketinganalyticsdrilldownlevel
- name: MarketingAnalyticsItem
  property_count: 7
  slug: posthog-marketinganalyticsitem
- name: MarketingAnalyticsOrderByEnum
  property_count: 0
  slug: posthog-marketinganalyticsorderbyenum
- name: MarketingAnalyticsTableQuery
  property_count: 25
  slug: posthog-marketinganalyticstablequery
- name: MarketingAnalyticsTableQueryResponse
  property_count: 13
  slug: posthog-marketinganalyticstablequeryresponse
- name: MarkToleratedInput
  property_count: 1
  slug: posthog-marktoleratedinput
- name: MatchedOn
  property_count: 0
  slug: posthog-matchedon
- name: MatchedOnEnum
  property_count: 0
  slug: posthog-matchedonenum
- name: MatchedRecording
  property_count: 2
  slug: posthog-matchedrecording
- name: MatchedRecordingEvent
  property_count: 2
  slug: posthog-matchedrecordingevent
- name: MaterializationMode
  property_count: 0
  slug: posthog-materializationmode
- name: MaterializationPreviewRequest
  property_count: 2
  slug: posthog-materializationpreviewrequest
- name: MaterializationType
  property_count: 0
  slug: posthog-materializationtype
- name: MaterializedColumnsOptimizationMode
  property_count: 0
  slug: posthog-materializedcolumnsoptimizationmode
- name: MathEnum
  property_count: 0
  slug: posthog-mathenum
- name: MathGroupTypeIndex
  property_count: 0
  slug: posthog-mathgrouptypeindex
- name: MCPAuthTypeEnum
  property_count: 0
  slug: posthog-mcpauthtypeenum
- name: MCPServerInstallation
  property_count: 15
  slug: posthog-mcpserverinstallation
- name: MCPServerInstallationTool
  property_count: 10
  slug: posthog-mcpserverinstallationtool
- name: MCPServerInstallationToolApprovalStateEnum
  property_count: 0
  slug: posthog-mcpserverinstallationtoolapprovalstateenum
- name: MCPServerTemplate
  property_count: 8
  slug: posthog-mcpservertemplate
- name: MeanRetentionCalculation
  property_count: 0
  slug: posthog-meanretentioncalculation
- name: MeetingPlatformEnum
  property_count: 0
  slug: posthog-meetingplatformenum
- name: Merge
  property_count: 3
  slug: posthog-merge
- name: Message
  property_count: 10
  slug: posthog-message
- name: MessageMinimal
  property_count: 1
  slug: posthog-messageminimal
- name: MessageSentiment
  property_count: 3
  slug: posthog-messagesentiment
- name: Method
  property_count: 0
  slug: posthog-method
- name: MethodEnum
  property_count: 0
  slug: posthog-methodenum
- name: Metric
  property_count: 0
  slug: posthog-metric
- name: Metrics
  property_count: 6
  slug: posthog-metrics
- name: MinimalFeatureFlag
  property_count: 13
  slug: posthog-minimalfeatureflag
- name: MinimalHedgehogConfig
  property_count: 4
  slug: posthog-minimalhedgehogconfig
- name: MinimalPerson
  property_count: 7
  slug: posthog-minimalperson
- name: ModelConfiguration
  property_count: 4
  slug: posthog-modelconfiguration
- name: ModelEnum
  property_count: 0
  slug: posthog-modelenum
- name: MultipleBreakdownOptions
  property_count: 1
  slug: posthog-multiplebreakdownoptions
- name: MultipleBreakdownType
  property_count: 0
  slug: posthog-multiplebreakdowntype
- name: MultipleVariantHandling
  property_count: 0
  slug: posthog-multiplevarianthandling
- name: MyFlagsResponse
  property_count: 2
  slug: posthog-myflagsresponse
- name: NetworkAccessLevelEnum
  property_count: 0
  slug: posthog-networkaccesslevelenum
- name: NonIntegratedConversionsTableQuery
  property_count: 23
  slug: posthog-nonintegratedconversionstablequery
- name: NonIntegratedConversionsTableQueryResponse
  property_count: 13
  slug: posthog-nonintegratedconversionstablequeryresponse
- name: Notebook
  property_count: 13
  slug: posthog-notebook
- name: NotebookCollabSave
  property_count: 7
  slug: posthog-notebookcollabsave
- name: NotebookMinimal
  property_count: 10
  slug: posthog-notebookminimal
- name: NotificationDestinationTypeEnum
  property_count: 0
  slug: posthog-notificationdestinationtypeenum
- name: NullEnum
  property_count: 0
  slug: posthog-nullenum
- name: NumericMetric
  property_count: 3
  slug: posthog-numericmetric
- name: NumericPropertyFilter
  property_count: 4
  slug: posthog-numericpropertyfilter
- name: NumericPropertyFilterOperatorEnum
  property_count: 0
  slug: posthog-numericpropertyfilteroperatorenum
- name: NumericScoreDefinitionConfig
  property_count: 3
  slug: posthog-numericscoredefinitionconfig
- name: OAuthRedirectResponse
  property_count: 1
  slug: posthog-oauthredirectresponse
- name: ObjectMediaPreview
  property_count: 9
  slug: posthog-objectmediapreview
- name: OCSVMDetectorConfig
  property_count: 6
  slug: posthog-ocsvmdetectorconfig
- name: OnErrorEnum
  property_count: 0
  slug: posthog-onerrorenum
- name: OrderBy
  property_count: 0
  slug: posthog-orderby
- name: OrderByEnum
  property_count: 0
  slug: posthog-orderbyenum
- name: OrderDirection1
  property_count: 0
  slug: posthog-orderdirection1
- name: OrderDirection2
  property_count: 0
  slug: posthog-orderdirection2
- name: Organization
  property_count: 26
  slug: posthog-organization
- name: OrganizationBasic
  property_count: 9
  slug: posthog-organizationbasic
- name: OrganizationDomain
  property_count: 15
  slug: posthog-organizationdomain
- name: OrganizationIntegration
  property_count: 7
  slug: posthog-organizationintegration
- name: OrganizationIntegrationKindEnum
  property_count: 0
  slug: posthog-organizationintegrationkindenum
- name: OrganizationInvite
  property_count: 13
  slug: posthog-organizationinvite
- name: OrganizationMember
  property_count: 8
  slug: posthog-organizationmember
- name: OrganizationMembershipLevelEnum
  property_count: 0
  slug: posthog-organizationmembershiplevelenum
- name: OrganizationOAuthApplication
  property_count: 7
  slug: posthog-organizationoauthapplication
- name: OriginEnum
  property_count: 0
  slug: posthog-originenum
- name: OriginProductEnum
  property_count: 0
  slug: posthog-originproductenum
- name: Outcome
  property_count: 2
  slug: posthog-outcome
- name: OutdatedTrafficAlert
  property_count: 2
  slug: posthog-outdatedtrafficalert
- name: OutputTypeEnum
  property_count: 0
  slug: posthog-outputtypeenum
- name: OverallHealthEnum
  property_count: 0
  slug: posthog-overallhealthenum
- name: PageURL
  property_count: 1
  slug: posthog-pageurl
- name: PaginatedActionList
  property_count: 4
  slug: posthog-paginatedactionlist
- name: PaginatedActivityLogList
  property_count: 4
  slug: posthog-paginatedactivityloglist
- name: PaginatedAlertList
  property_count: 4
  slug: posthog-paginatedalertlist
- name: PaginatedAnnotationList
  property_count: 4
  slug: posthog-paginatedannotationlist
- name: PaginatedApprovalPolicyList
  property_count: 4
  slug: posthog-paginatedapprovalpolicylist
- name: PaginatedAsyncDeletionStatusList
  property_count: 4
  slug: posthog-paginatedasyncdeletionstatuslist
- name: PaginatedBatchExportBackfillList
  property_count: 3
  slug: posthog-paginatedbatchexportbackfilllist
- name: PaginatedBatchExportList
  property_count: 4
  slug: posthog-paginatedbatchexportlist
- name: PaginatedBatchExportRunList
  property_count: 3
  slug: posthog-paginatedbatchexportrunlist
- name: PaginatedChangeRequestList
  property_count: 4
  slug: posthog-paginatedchangerequestlist
- name: PaginatedClickhouseEventList
  property_count: 2
  slug: posthog-paginatedclickhouseeventlist
- name: PaginatedClusteringJobList
  property_count: 4
  slug: posthog-paginatedclusteringjoblist
- name: PaginatedCohortList
  property_count: 4
  slug: posthog-paginatedcohortlist
- name: PaginatedCommentList
  property_count: 3
  slug: posthog-paginatedcommentlist
- name: PaginatedConversationMinimalList
  property_count: 4
  slug: posthog-paginatedconversationminimallist
- name: PaginatedCustomerJourneyList
  property_count: 4
  slug: posthog-paginatedcustomerjourneylist
- name: PaginatedCustomerProfileConfigList
  property_count: 4
  slug: posthog-paginatedcustomerprofileconfiglist
- name: PaginatedDashboardBasicList
  property_count: 4
  slug: posthog-paginateddashboardbasiclist
- name: PaginatedDashboardTemplateList
  property_count: 4
  slug: posthog-paginateddashboardtemplatelist
- name: PaginatedDataColorThemeList
  property_count: 4
  slug: posthog-paginateddatacolorthemelist
- name: PaginatedDataModelingJobList
  property_count: 3
  slug: posthog-paginateddatamodelingjoblist
- name: PaginatedDatasetItemList
  property_count: 4
  slug: posthog-paginateddatasetitemlist
- name: PaginatedDatasetList
  property_count: 4
  slug: posthog-paginateddatasetlist
- name: PaginatedDataWarehouseModelPathList
  property_count: 4
  slug: posthog-paginateddatawarehousemodelpathlist
- name: PaginatedDataWarehouseSavedQueryMinimalList
  property_count: 4
  slug: posthog-paginateddatawarehousesavedqueryminimallist
- name: PaginatedDesktopRecordingList
  property_count: 4
  slug: posthog-paginateddesktoprecordinglist
- name: PaginatedEarlyAccessFeatureList
  property_count: 4
  slug: posthog-paginatedearlyaccessfeaturelist
- name: PaginatedElementList
  property_count: 4
  slug: posthog-paginatedelementlist
- name: PaginatedEndpointResponseList
  property_count: 4
  slug: posthog-paginatedendpointresponselist
- name: PaginatedEndpointVersionResponseList
  property_count: 4
  slug: posthog-paginatedendpointversionresponselist
- name: PaginatedEnterpriseEventDefinitionList
  property_count: 4
  slug: posthog-paginatedenterpriseeventdefinitionlist
- name: PaginatedEnterprisePropertyDefinitionList
  property_count: 4
  slug: posthog-paginatedenterprisepropertydefinitionlist
- name: PaginatedErrorTrackingAssignmentRuleList
  property_count: 4
  slug: posthog-paginatederrortrackingassignmentrulelist
- name: PaginatedErrorTrackingFingerprintList
  property_count: 4
  slug: posthog-paginatederrortrackingfingerprintlist
- name: PaginatedErrorTrackingIssueFullList
  property_count: 4
  slug: posthog-paginatederrortrackingissuefulllist
- name: PaginatedErrorTrackingRecommendationList
  property_count: 4
  slug: posthog-paginatederrortrackingrecommendationlist
- name: PaginatedErrorTrackingReleaseList
  property_count: 4
  slug: posthog-paginatederrortrackingreleaselist
- name: PaginatedErrorTrackingSpikeEventList
  property_count: 4
  slug: posthog-paginatederrortrackingspikeeventlist
- name: PaginatedErrorTrackingStackFrameList
  property_count: 4
  slug: posthog-paginatederrortrackingstackframelist
- name: PaginatedErrorTrackingSuppressionRuleList
  property_count: 4
  slug: posthog-paginatederrortrackingsuppressionrulelist
- name: PaginatedErrorTrackingSymbolSetList
  property_count: 4
  slug: posthog-paginatederrortrackingsymbolsetlist
- name: PaginatedEvaluationList
  property_count: 4
  slug: posthog-paginatedevaluationlist
- name: PaginatedEvaluationReportList
  property_count: 4
  slug: posthog-paginatedevaluationreportlist
- name: PaginatedEvaluationReportRunList
  property_count: 4
  slug: posthog-paginatedevaluationreportrunlist
- name: PaginatedEventSchemaList
  property_count: 4
  slug: posthog-paginatedeventschemalist
- name: PaginatedExperimentHoldoutList
  property_count: 4
  slug: posthog-paginatedexperimentholdoutlist
- name: PaginatedExperimentList
  property_count: 4
  slug: posthog-paginatedexperimentlist
- name: PaginatedExperimentSavedMetricList
  property_count: 4
  slug: posthog-paginatedexperimentsavedmetriclist
- name: PaginatedExportedAssetList
  property_count: 4
  slug: posthog-paginatedexportedassetlist
- name: PaginatedExternalDataSchemaList
  property_count: 4
  slug: posthog-paginatedexternaldataschemalist
- name: PaginatedExternalDataSourceConnectionOptionList
  property_count: 4
  slug: posthog-paginatedexternaldatasourceconnectionoptionlist
- name: PaginatedExternalDataSourceSerializersList
  property_count: 4
  slug: posthog-paginatedexternaldatasourceserializerslist
- name: PaginatedFeatureFlagList
  property_count: 4
  slug: posthog-paginatedfeatureflaglist
- name: PaginatedFileSystemList
  property_count: 4
  slug: posthog-paginatedfilesystemlist
- name: PaginatedFileSystemShortcutList
  property_count: 4
  slug: posthog-paginatedfilesystemshortcutlist
- name: PaginatedGroupList
  property_count: 3
  slug: posthog-paginatedgrouplist
- name: PaginatedGroupUsageMetricList
  property_count: 4
  slug: posthog-paginatedgroupusagemetriclist
- name: PaginatedHealthIssueList
  property_count: 4
  slug: posthog-paginatedhealthissuelist
- name: PaginatedHeatmapScreenshotResponseList
  property_count: 4
  slug: posthog-paginatedheatmapscreenshotresponselist
- name: PaginatedHeatmapsResponseList
  property_count: 4
  slug: posthog-paginatedheatmapsresponselist
- name: PaginatedHogFlowMinimalList
  property_count: 4
  slug: posthog-paginatedhogflowminimallist
- name: PaginatedHogFlowScheduleList
  property_count: 4
  slug: posthog-paginatedhogflowschedulelist
- name: PaginatedHogFunctionMinimalList
  property_count: 4
  slug: posthog-paginatedhogfunctionminimallist
- name: PaginatedHogFunctionTemplateList
  property_count: 4
  slug: posthog-paginatedhogfunctiontemplatelist
- name: PaginatedInsightList
  property_count: 4
  slug: posthog-paginatedinsightlist
- name: PaginatedInsightVariableList
  property_count: 4
  slug: posthog-paginatedinsightvariablelist
- name: PaginatedIntegrationConfigList
  property_count: 4
  slug: posthog-paginatedintegrationconfiglist
- name: PaginatedLegalDocumentDTOList
  property_count: 4
  slug: posthog-paginatedlegaldocumentdtolist
- name: PaginatedLiveDebuggerBreakpointList
  property_count: 4
  slug: posthog-paginatedlivedebuggerbreakpointlist
- name: PaginatedLLMPromptListList
  property_count: 4
  slug: posthog-paginatedllmpromptlistlist
- name: PaginatedLLMProviderKeyList
  property_count: 4
  slug: posthog-paginatedllmproviderkeylist
- name: PaginatedLLMSkillListList
  property_count: 4
  slug: posthog-paginatedllmskilllistlist
- name: PaginatedLogsAlertConfigurationList
  property_count: 4
  slug: posthog-paginatedlogsalertconfigurationlist
- name: PaginatedLogsAlertEventList
  property_count: 4
  slug: posthog-paginatedlogsalerteventlist
- name: PaginatedLogsSamplingRuleList
  property_count: 4
  slug: posthog-paginatedlogssamplingrulelist
- name: PaginatedLogsViewList
  property_count: 4
  slug: posthog-paginatedlogsviewlist
- name: PaginatedMCPServerInstallationList
  property_count: 4
  slug: posthog-paginatedmcpserverinstallationlist
- name: PaginatedMCPServerInstallationToolList
  property_count: 4
  slug: posthog-paginatedmcpserverinstallationtoollist
- name: PaginatedMCPServerTemplateList
  property_count: 4
  slug: posthog-paginatedmcpservertemplatelist
- name: PaginatedNotebookMinimalList
  property_count: 4
  slug: posthog-paginatednotebookminimallist
- name: PaginatedObjectMediaPreviewList
  property_count: 4
  slug: posthog-paginatedobjectmediapreviewlist
- name: PaginatedOrganizationDomainList
  property_count: 4
  slug: posthog-paginatedorganizationdomainlist
- name: PaginatedOrganizationIntegrationList
  property_count: 4
  slug: posthog-paginatedorganizationintegrationlist
- name: PaginatedOrganizationInviteList
  property_count: 4
  slug: posthog-paginatedorganizationinvitelist
- name: PaginatedOrganizationList
  property_count: 4
  slug: posthog-paginatedorganizationlist
- name: PaginatedOrganizationMemberList
  property_count: 4
  slug: posthog-paginatedorganizationmemberlist
- name: PaginatedOrganizationOAuthApplicationList
  property_count: 4
  slug: posthog-paginatedorganizationoauthapplicationlist
- name: PaginatedPauseStateResponseList
  property_count: 4
  slug: posthog-paginatedpausestateresponselist
- name: PaginatedPersistedFolderList
  property_count: 4
  slug: posthog-paginatedpersistedfolderlist
- name: PaginatedPersonRecordList
  property_count: 4
  slug: posthog-paginatedpersonrecordlist
- name: PaginatedPluginLogEntryList
  property_count: 4
  slug: posthog-paginatedpluginlogentrylist
- name: PaginatedProductTourList
  property_count: 4
  slug: posthog-paginatedproducttourlist
- name: PaginatedProjectBackwardCompatBasicList
  property_count: 4
  slug: posthog-paginatedprojectbackwardcompatbasiclist
- name: PaginatedProjectSecretAPIKeyList
  property_count: 4
  slug: posthog-paginatedprojectsecretapikeylist
- name: PaginatedQuarantinedIdentifierEntryList
  property_count: 4
  slug: posthog-paginatedquarantinedidentifierentrylist
- name: PaginatedRepoList
  property_count: 4
  slug: posthog-paginatedrepolist
- name: PaginatedReviewQueueItemList
  property_count: 4
  slug: posthog-paginatedreviewqueueitemlist
- name: PaginatedReviewQueueList
  property_count: 4
  slug: posthog-paginatedreviewqueuelist
- name: PaginatedRoleExternalReferenceList
  property_count: 4
  slug: posthog-paginatedroleexternalreferencelist
- name: PaginatedRoleList
  property_count: 4
  slug: posthog-paginatedrolelist
- name: PaginatedRoleMembershipList
  property_count: 4
  slug: posthog-paginatedrolemembershiplist
- name: PaginatedRunList
  property_count: 4
  slug: posthog-paginatedrunlist
- name: PaginatedSandboxEnvironmentListList
  property_count: 4
  slug: posthog-paginatedsandboxenvironmentlistlist
- name: PaginatedSchemaPropertyGroupList
  property_count: 4
  slug: posthog-paginatedschemapropertygrouplist
- name: PaginatedScoreDefinitionList
  property_count: 4
  slug: posthog-paginatedscoredefinitionlist
- name: PaginatedSessionGroupSummaryMinimalList
  property_count: 4
  slug: posthog-paginatedsessiongroupsummaryminimallist
- name: PaginatedSessionRecordingList
  property_count: 4
  slug: posthog-paginatedsessionrecordinglist
- name: PaginatedSessionRecordingPlaylistList
  property_count: 4
  slug: posthog-paginatedsessionrecordingplaylistlist
- name: PaginatedSignalReportList
  property_count: 4
  slug: posthog-paginatedsignalreportlist
- name: PaginatedSignalSourceConfigList
  property_count: 4
  slug: posthog-paginatedsignalsourceconfiglist
- name: PaginatedSnapshotHistoryEntryList
  property_count: 4
  slug: posthog-paginatedsnapshothistoryentrylist
- name: PaginatedSnapshotList
  property_count: 4
  slug: posthog-paginatedsnapshotlist
- name: PaginatedSubscriptionDeliveryList
  property_count: 3
  slug: posthog-paginatedsubscriptiondeliverylist
- name: PaginatedSubscriptionList
  property_count: 4
  slug: posthog-paginatedsubscriptionlist
- name: PaginatedSurveyList
  property_count: 4
  slug: posthog-paginatedsurveylist
- name: PaginatedTableList
  property_count: 4
  slug: posthog-paginatedtablelist
- name: PaginatedTaggerList
  property_count: 4
  slug: posthog-paginatedtaggerlist
- name: PaginatedTaskAutomationList
  property_count: 4
  slug: posthog-paginatedtaskautomationlist
- name: PaginatedTaskList
  property_count: 4
  slug: posthog-paginatedtasklist
- name: PaginatedTaskRunDetailList
  property_count: 4
  slug: posthog-paginatedtaskrundetaillist
- name: PaginatedTeamBasicList
  property_count: 4
  slug: posthog-paginatedteambasiclist
- name: PaginatedThresholdWithAlertList
  property_count: 4
  slug: posthog-paginatedthresholdwithalertlist
- name: PaginatedTicketList
  property_count: 4
  slug: posthog-paginatedticketlist
- name: PaginatedTicketViewList
  property_count: 4
  slug: posthog-paginatedticketviewlist
- name: PaginatedToleratedHashEntryList
  property_count: 4
  slug: posthog-paginatedtoleratedhashentrylist
- name: PaginatedTraceReviewList
  property_count: 4
  slug: posthog-paginatedtracereviewlist
- name: PaginatedUserGitHubIntegrationListResponseList
  property_count: 4
  slug: posthog-paginatedusergithubintegrationlistresponselist
- name: PaginatedUserInterviewList
  property_count: 4
  slug: posthog-paginateduserinterviewlist
- name: PaginatedUserList
  property_count: 4
  slug: posthog-paginateduserlist
- name: PaginatedViewLinkList
  property_count: 4
  slug: posthog-paginatedviewlinklist
- name: PaginatedWebExperimentsAPIList
  property_count: 4
  slug: posthog-paginatedwebexperimentsapilist
- name: PatchedAction
  property_count: 19
  slug: posthog-patchedaction
- name: PatchedAddPersonsToStaticCohortRequest
  property_count: 1
  slug: posthog-patchedaddpersonstostaticcohortrequest
- name: PatchedAlert
  property_count: 25
  slug: posthog-patchedalert
- name: PatchedAnnotation
  property_count: 15
  slug: posthog-patchedannotation
- name: PatchedApprovalPolicy
  property_count: 12
  slug: posthog-patchedapprovalpolicy
- name: PatchedBatchExport
  property_count: 19
  slug: posthog-patchedbatchexport
- name: PatchedClusteringJob
  property_count: 7
  slug: posthog-patchedclusteringjob
- name: PatchedCohort
  property_count: 22
  slug: posthog-patchedcohort
- name: PatchedComment
  property_count: 13
  slug: posthog-patchedcomment
- name: PatchedConversation
  property_count: 15
  slug: posthog-patchedconversation
- name: PatchedCustomerJourney
  property_count: 7
  slug: posthog-patchedcustomerjourney
- name: PatchedCustomerProfileConfig
  property_count: 6
  slug: posthog-patchedcustomerprofileconfig
- name: PatchedDashboard
  property_count: 31
  slug: posthog-patcheddashboard
- name: PatchedDashboardTemplate
  property_count: 15
  slug: posthog-patcheddashboardtemplate
- name: PatchedDataColorTheme
  property_count: 6
  slug: posthog-patcheddatacolortheme
- name: PatchedDataset
  property_count: 9
  slug: posthog-patcheddataset
- name: PatchedDatasetItem
  property_count: 13
  slug: posthog-patcheddatasetitem
- name: PatchedDataWarehouseSavedQuery
  property_count: 23
  slug: posthog-patcheddatawarehousesavedquery
- name: PatchedDataWarehouseSavedQueryFolder
  property_count: 6
  slug: posthog-patcheddatawarehousesavedqueryfolder
- name: PatchedDesktopRecording
  property_count: 25
  slug: posthog-patcheddesktoprecording
- name: PatchedEarlyAccessFeature
  property_count: 8
  slug: posthog-patchedearlyaccessfeature
- name: PatchedElement
  property_count: 9
  slug: posthog-patchedelement
- name: PatchedEndpointRequest
  property_count: 10
  slug: posthog-patchedendpointrequest
- name: PatchedEnterpriseEventDefinition
  property_count: 24
  slug: posthog-patchedenterpriseeventdefinition
- name: PatchedEnterprisePropertyDefinition
  property_count: 13
  slug: posthog-patchedenterprisepropertydefinition
- name: PatchedErrorTrackingAssignmentRule
  property_count: 7
  slug: posthog-patchederrortrackingassignmentrule
- name: PatchedErrorTrackingAssignmentRuleUpdateRequest
  property_count: 2
  slug: posthog-patchederrortrackingassignmentruleupdaterequest
- name: PatchedErrorTrackingGroupingRule
  property_count: 9
  slug: posthog-patchederrortrackinggroupingrule
- name: PatchedErrorTrackingIssueFull
  property_count: 8
  slug: posthog-patchederrortrackingissuefull
- name: PatchedErrorTrackingRelease
  property_count: 7
  slug: posthog-patchederrortrackingrelease
- name: PatchedErrorTrackingSpikeDetectionConfig
  property_count: 3
  slug: posthog-patchederrortrackingspikedetectionconfig
- name: PatchedErrorTrackingSuppressionRule
  property_count: 7
  slug: posthog-patchederrortrackingsuppressionrule
- name: PatchedErrorTrackingSymbolSet
  property_count: 8
  slug: posthog-patchederrortrackingsymbolset
- name: PatchedEvaluation
  property_count: 16
  slug: posthog-patchedevaluation
- name: PatchedEvaluationReport
  property_count: 18
  slug: posthog-patchedevaluationreport
- name: PatchedEventSchema
  property_count: 6
  slug: posthog-patchedeventschema
- name: PatchedExperiment
  property_count: 36
  slug: posthog-patchedexperiment
- name: PatchedExperimentHoldout
  property_count: 7
  slug: posthog-patchedexperimentholdout
- name: PatchedExperimentSavedMetric
  property_count: 9
  slug: posthog-patchedexperimentsavedmetric
- name: PatchedExternalDataSchema
  property_count: 17
  slug: posthog-patchedexternaldataschema
- name: PatchedExternalDataSourceBulkUpdateSchemas
  property_count: 1
  slug: posthog-patchedexternaldatasourcebulkupdateschemas
- name: PatchedExternalDataSourceSerializers
  property_count: 19
  slug: posthog-patchedexternaldatasourceserializers
- name: PatchedFeatureFlagPartialUpdateRequestSchema
  property_count: 6
  slug: posthog-patchedfeatureflagpartialupdaterequestschema
- name: PatchedFileSystem
  property_count: 10
  slug: posthog-patchedfilesystem
- name: PatchedFileSystemShortcut
  property_count: 7
  slug: posthog-patchedfilesystemshortcut
- name: PatchedGroupType
  property_count: 7
  slug: posthog-patchedgrouptype
- name: PatchedGroupUsageMetric
  property_count: 8
  slug: posthog-patchedgroupusagemetric
- name: PatchedHealthIssue
  property_count: 9
  slug: posthog-patchedhealthissue
- name: PatchedHeatmapScreenshotResponse
  property_count: 15
  slug: posthog-patchedheatmapscreenshotresponse
- name: PatchedHogFlow
  property_count: 17
  slug: posthog-patchedhogflow
- name: PatchedHogFunction
  property_count: 24
  slug: posthog-patchedhogfunction
- name: PatchedHogFunctionRearrange
  property_count: 1
  slug: posthog-patchedhogfunctionrearrange
- name: PatchedInsight
  property_count: 36
  slug: posthog-patchedinsight
- name: PatchedInsightVariable
  property_count: 8
  slug: posthog-patchedinsightvariable
- name: PatchedIntegrationConfig
  property_count: 7
  slug: posthog-patchedintegrationconfig
- name: PatchedJsSnippetVersion
  property_count: 1
  slug: posthog-patchedjssnippetversion
- name: PatchedLiveDebuggerBreakpoint
  property_count: 8
  slug: posthog-patchedlivedebuggerbreakpoint
- name: PatchedLLMPromptPublish
  property_count: 3
  slug: posthog-patchedllmpromptpublish
- name: PatchedLLMProviderKey
  property_count: 15
  slug: posthog-patchedllmproviderkey
- name: PatchedLLMSkillPublish
  property_count: 10
  slug: posthog-patchedllmskillpublish
- name: PatchedLogsAlertConfiguration
  property_count: 24
  slug: posthog-patchedlogsalertconfiguration
- name: PatchedLogsSamplingRule
  property_count: 13
  slug: posthog-patchedlogssamplingrule
- name: PatchedLogsView
  property_count: 8
  slug: posthog-patchedlogsview
- name: PatchedMCPServerInstallationUpdate
  property_count: 3
  slug: posthog-patchedmcpserverinstallationupdate
- name: PatchedNotebook
  property_count: 13
  slug: posthog-patchednotebook
- name: PatchedObjectMediaPreview
  property_count: 9
  slug: posthog-patchedobjectmediapreview
- name: PatchedOrganization
  property_count: 26
  slug: posthog-patchedorganization
- name: PatchedOrganizationDomain
  property_count: 15
  slug: posthog-patchedorganizationdomain
- name: PatchedOrganizationIntegration
  property_count: 7
  slug: posthog-patchedorganizationintegration
- name: PatchedOrganizationMember
  property_count: 8
  slug: posthog-patchedorganizationmember
- name: PatchedPersistedFolder
  property_count: 6
  slug: posthog-patchedpersistedfolder
- name: PatchedPersonRecord
  property_count: 7
  slug: posthog-patchedpersonrecord
- name: PatchedPinnedSceneTabs
  property_count: 2
  slug: posthog-patchedpinnedscenetabs
- name: PatchedProductTourSerializerCreateUpdateOnly
  property_count: 16
  slug: posthog-patchedproducttourserializercreateupdateonly
- name: PatchedProjectBackwardCompat
  property_count: 69
  slug: posthog-patchedprojectbackwardcompat
- name: PatchedProjectSecretAPIKey
  property_count: 9
  slug: posthog-patchedprojectsecretapikey
- name: PatchedRemovePersonRequest
  property_count: 1
  slug: posthog-patchedremovepersonrequest
- name: PatchedReviewQueueItemUpdate
  property_count: 1
  slug: posthog-patchedreviewqueueitemupdate
- name: PatchedReviewQueueUpdate
  property_count: 1
  slug: posthog-patchedreviewqueueupdate
- name: PatchedRole
  property_count: 6
  slug: posthog-patchedrole
- name: PatchedSandboxEnvironment
  property_count: 14
  slug: posthog-patchedsandboxenvironment
- name: PatchedSchemaPropertyGroup
  property_count: 8
  slug: posthog-patchedschemapropertygroup
- name: PatchedScoreDefinitionMetadata
  property_count: 3
  slug: posthog-patchedscoredefinitionmetadata
- name: PatchedSessionGroupSummary
  property_count: 9
  slug: posthog-patchedsessiongroupsummary
- name: PatchedSessionRecording
  property_count: 27
  slug: posthog-patchedsessionrecording
- name: PatchedSessionRecordingPlaylist
  property_count: 16
  slug: posthog-patchedsessionrecordingplaylist
- name: PatchedSessionSummariesConfig
  property_count: 1
  slug: posthog-patchedsessionsummariesconfig
- name: PatchedSignalSourceConfig
  property_count: 8
  slug: posthog-patchedsignalsourceconfig
- name: PatchedSubscription
  property_count: 25
  slug: posthog-patchedsubscription
- name: PatchedSurveySerializerCreateUpdateOnlySchema
  property_count: 37
  slug: posthog-patchedsurveyserializercreateupdateonlyschema
- name: PatchedTable
  property_count: 13
  slug: posthog-patchedtable
- name: PatchedTagger
  property_count: 12
  slug: posthog-patchedtagger
- name: PatchedTask
  property_count: 19
  slug: posthog-patchedtask
- name: PatchedTaskAutomation
  property_count: 16
  slug: posthog-patchedtaskautomation
- name: PatchedTaskRunSetOutputRequest
  property_count: 1
  slug: posthog-patchedtaskrunsetoutputrequest
- name: PatchedTaskRunUpdate
  property_count: 8
  slug: posthog-patchedtaskrunupdate
- name: PatchedTeam
  property_count: 85
  slug: posthog-patchedteam
- name: PatchedTicket
  property_count: 31
  slug: posthog-patchedticket
- name: PatchedToolApprovalUpdate
  property_count: 1
  slug: posthog-patchedtoolapprovalupdate
- name: PatchedTraceReviewUpdate
  property_count: 4
  slug: posthog-patchedtracereviewupdate
- name: PatchedUpdateRepoRequestInput
  property_count: 2
  slug: posthog-patchedupdatereporequestinput
- name: PatchedUser
  property_count: 40
  slug: posthog-patcheduser
- name: PatchedUserInterview
  property_count: 7
  slug: posthog-patcheduserinterview
- name: PatchedViewLink
  property_count: 10
  slug: posthog-patchedviewlink
- name: PatchedWebExperimentsAPI
  property_count: 5
  slug: posthog-patchedwebexperimentsapi
- name: PathCleaningFilter
  property_count: 3
  slug: posthog-pathcleaningfilter
- name: PathsFilter
  property_count: 16
  slug: posthog-pathsfilter
- name: PathsLink
  property_count: 4
  slug: posthog-pathslink
- name: PathsQuery
  property_count: 13
  slug: posthog-pathsquery
- name: PathsQueryResponse
  property_count: 7
  slug: posthog-pathsqueryresponse
- name: PathType
  property_count: 0
  slug: posthog-pathtype
- name: PauseResponse
  property_count: 2
  slug: posthog-pauseresponse
- name: PauseStateResponse
  property_count: 1
  slug: posthog-pausestateresponse
- name: PauseUntilRequest
  property_count: 1
  slug: posthog-pauseuntilrequest
- name: PCADetectorConfig
  property_count: 4
  slug: posthog-pcadetectorconfig
- name: PendingInvite
  property_count: 5
  slug: posthog-pendinginvite
- name: PersistedFolder
  property_count: 6
  slug: posthog-persistedfolder
- name: PersistedFolderTypeEnum
  property_count: 0
  slug: posthog-persistedfoldertypeenum
- name: Person
  property_count: 3
  slug: posthog-person
- name: PersonBulkDeleteRequest
  property_count: 5
  slug: posthog-personbulkdeleterequest
- name: PersonBulkDeleteResponse
  property_count: 5
  slug: posthog-personbulkdeleteresponse
- name: PersonDeletePropertyRequest
  property_count: 1
  slug: posthog-persondeletepropertyrequest
- name: PersonFilter
  property_count: 8
  slug: posthog-personfilter
- name: PersonPropertiesAtTimeDebug
  property_count: 5
  slug: posthog-personpropertiesattimedebug
- name: PersonPropertiesAtTimeMetadata
  property_count: 7
  slug: posthog-personpropertiesattimemetadata
- name: PersonPropertiesAtTimeResponse
  property_count: 9
  slug: posthog-personpropertiesattimeresponse
- name: PersonPropertyFilter
  property_count: 5
  slug: posthog-personpropertyfilter
- name: PersonRecord
  property_count: 7
  slug: posthog-personrecord
- name: PersonsArgMaxVersion
  property_count: 0
  slug: posthog-personsargmaxversion
- name: PersonsJoinMode
  property_count: 0
  slug: posthog-personsjoinmode
- name: PersonsNode
  property_count: 12
  slug: posthog-personsnode
- name: PersonsOnEventsMode
  property_count: 0
  slug: posthog-personsoneventsmode
- name: PersonType
  property_count: 8
  slug: posthog-persontype
- name: PersonUpdatePropertyRequest
  property_count: 2
  slug: posthog-personupdatepropertyrequest
- name: PinnedSceneTab
  property_count: 11
  slug: posthog-pinnedscenetab
- name: PinnedSceneTabs
  property_count: 2
  slug: posthog-pinnedscenetabs
- name: PluginLogEntry
  property_count: 9
  slug: posthog-pluginlogentry
- name: PluginLogEntrySourceEnum
  property_count: 0
  slug: posthog-pluginlogentrysourceenum
- name: PluginLogEntryTypeEnum
  property_count: 0
  slug: posthog-pluginlogentrytypeenum
- name: PluginsAccessLevelEnum
  property_count: 0
  slug: posthog-pluginsaccesslevelenum
- name: Population
  property_count: 4
  slug: posthog-population
- name: Position
  property_count: 0
  slug: posthog-position
- name: PrAuthorshipModeEnum
  property_count: 0
  slug: posthog-prauthorshipmodeenum
- name: PrecomputationMode
  property_count: 0
  slug: posthog-precomputationmode
- name: PreprocessingConfig
  property_count: 3
  slug: posthog-preprocessingconfig
- name: PriorityEnum
  property_count: 0
  slug: posthog-priorityenum
- name: ProductTour
  property_count: 16
  slug: posthog-producttour
- name: ProductTourSerializerCreateUpdateOnly
  property_count: 16
  slug: posthog-producttourserializercreateupdateonly
- name: ProductTourSerializerCreateUpdateOnlyCreationContextEnum
  property_count: 0
  slug: posthog-producttourserializercreateupdateonlycreationcontextenum
- name: ProjectBackwardCompat
  property_count: 69
  slug: posthog-projectbackwardcompat
- name: ProjectBackwardCompatBasic
  property_count: 11
  slug: posthog-projectbackwardcompatbasic
- name: ProjectSecretAPIKey
  property_count: 9
  slug: posthog-projectsecretapikey
- name: PromotedPropertiesResponse
  property_count: 1
  slug: posthog-promotedpropertiesresponse
- name: Property
  property_count: 2
  slug: posthog-property
- name: PropertyDefinitionTypeEnum
  property_count: 0
  slug: posthog-propertydefinitiontypeenum
- name: PropertyFilterTypeEnum
  property_count: 0
  slug: posthog-propertyfiltertypeenum
- name: PropertyGroupFilter
  property_count: 2
  slug: posthog-propertygroupfilter
- name: PropertyGroupFilterValue
  property_count: 2
  slug: posthog-propertygroupfiltervalue
- name: PropertyGroupOperator
  property_count: 0
  slug: posthog-propertygroupoperator
- name: PropertyGroupsMode
  property_count: 0
  slug: posthog-propertygroupsmode
- name: PropertyGroupTypeEnum
  property_count: 0
  slug: posthog-propertygrouptypeenum
- name: PropertyItem
  property_count: 4
  slug: posthog-propertyitem
- name: PropertyItemOperatorEnum
  property_count: 0
  slug: posthog-propertyitemoperatorenum
- name: PropertyMathType
  property_count: 0
  slug: posthog-propertymathtype
- name: PropertyOperator
  property_count: 0
  slug: posthog-propertyoperator
- name: PropertyType
  property_count: 0
  slug: posthog-propertytype
- name: PropertyValueItem
  property_count: 2
  slug: posthog-propertyvalueitem
- name: PropertyValuesQuery
  property_count: 10
  slug: posthog-propertyvaluesquery
- name: PropertyValuesQueryResponse
  property_count: 7
  slug: posthog-propertyvaluesqueryresponse
- name: ProvisionWarehouseRequest
  property_count: 1
  slug: posthog-provisionwarehouserequest
- name: ProvisionWarehouseResponse
  property_count: 2
  slug: posthog-provisionwarehouseresponse
- name: ProxyRecord
  property_count: 8
  slug: posthog-proxyrecord
- name: ProxyRecordListResponse
  property_count: 2
  slug: posthog-proxyrecordlistresponse
- name: ProxyRecordStatusEnum
  property_count: 0
  slug: posthog-proxyrecordstatusenum
- name: QuarantinedIdentifierEntry
  property_count: 8
  slug: posthog-quarantinedidentifierentry
- name: QuarantineInput
  property_count: 3
  slug: posthog-quarantineinput
- name: QueryIndexUsage
  property_count: 0
  slug: posthog-queryindexusage
- name: QueryLogTags
  property_count: 3
  slug: posthog-querylogtags
- name: QueryRequest
  property_count: 8
  slug: posthog-queryrequest
- name: QueryResponseAlternative
  property_count: 0
  slug: posthog-queryresponsealternative
- name: QueryResponseAlternative1
  property_count: 13
  slug: posthog-queryresponsealternative1
- name: QueryResponseAlternative10
  property_count: 3
  slug: posthog-queryresponsealternative10
- name: QueryResponseAlternative11
  property_count: 12
  slug: posthog-queryresponsealternative11
- name: QueryResponseAlternative14
  property_count: 11
  slug: posthog-queryresponsealternative14
- name: QueryResponseAlternative15
  property_count: 10
  slug: posthog-queryresponsealternative15
- name: QueryResponseAlternative16
  property_count: 7
  slug: posthog-queryresponsealternative16
- name: QueryResponseAlternative17
  property_count: 11
  slug: posthog-queryresponsealternative17
- name: QueryResponseAlternative18
  property_count: 10
  slug: posthog-queryresponsealternative18
- name: QueryResponseAlternative19
  property_count: 11
  slug: posthog-queryresponsealternative19
- name: QueryResponseAlternative2
  property_count: 12
  slug: posthog-queryresponsealternative2
- name: QueryResponseAlternative20
  property_count: 16
  slug: posthog-queryresponsealternative20
- name: QueryResponseAlternative21
  property_count: 6
  slug: posthog-queryresponsealternative21
- name: QueryResponseAlternative22
  property_count: 10
  slug: posthog-queryresponsealternative22
- name: QueryResponseAlternative23
  property_count: 11
  slug: posthog-queryresponsealternative23
- name: QueryResponseAlternative24
  property_count: 14
  slug: posthog-queryresponsealternative24
- name: QueryResponseAlternative25
  property_count: 13
  slug: posthog-queryresponsealternative25
- name: QueryResponseAlternative27
  property_count: 7
  slug: posthog-queryresponsealternative27
- name: QueryResponseAlternative28
  property_count: 9
  slug: posthog-queryresponsealternative28
- name: QueryResponseAlternative29
  property_count: 3
  slug: posthog-queryresponsealternative29
- name: QueryResponseAlternative3
  property_count: 13
  slug: posthog-queryresponsealternative3
- name: QueryResponseAlternative30
  property_count: 9
  slug: posthog-queryresponsealternative30
- name: QueryResponseAlternative31
  property_count: 8
  slug: posthog-queryresponsealternative31
- name: QueryResponseAlternative32
  property_count: 8
  slug: posthog-queryresponsealternative32
- name: QueryResponseAlternative33
  property_count: 8
  slug: posthog-queryresponsealternative33
- name: QueryResponseAlternative34
  property_count: 7
  slug: posthog-queryresponsealternative34
- name: QueryResponseAlternative35
  property_count: 8
  slug: posthog-queryresponsealternative35
- name: QueryResponseAlternative36
  property_count: 13
  slug: posthog-queryresponsealternative36
- name: QueryResponseAlternative37
  property_count: 8
  slug: posthog-queryresponsealternative37
- name: QueryResponseAlternative38
  property_count: 13
  slug: posthog-queryresponsealternative38
- name: QueryResponseAlternative39
  property_count: 13
  slug: posthog-queryresponsealternative39
- name: QueryResponseAlternative4
  property_count: 13
  slug: posthog-queryresponsealternative4
- name: QueryResponseAlternative40
  property_count: 13
  slug: posthog-queryresponsealternative40
- name: QueryResponseAlternative41
  property_count: 13
  slug: posthog-queryresponsealternative41
- name: QueryResponseAlternative42
  property_count: 16
  slug: posthog-queryresponsealternative42
- name: QueryResponseAlternative43
  property_count: 11
  slug: posthog-queryresponsealternative43
- name: QueryResponseAlternative44
  property_count: 14
  slug: posthog-queryresponsealternative44
- name: QueryResponseAlternative45
  property_count: 13
  slug: posthog-queryresponsealternative45
- name: QueryResponseAlternative47
  property_count: 7
  slug: posthog-queryresponsealternative47
- name: QueryResponseAlternative48
  property_count: 12
  slug: posthog-queryresponsealternative48
- name: QueryResponseAlternative49
  property_count: 12
  slug: posthog-queryresponsealternative49
- name: QueryResponseAlternative5
  property_count: 7
  slug: posthog-queryresponsealternative5
- name: QueryResponseAlternative50
  property_count: 8
  slug: posthog-queryresponsealternative50
- name: QueryResponseAlternative51
  property_count: 8
  slug: posthog-queryresponsealternative51
- name: QueryResponseAlternative52
  property_count: 8
  slug: posthog-queryresponsealternative52
- name: QueryResponseAlternative53
  property_count: 7
  slug: posthog-queryresponsealternative53
- name: QueryResponseAlternative54
  property_count: 8
  slug: posthog-queryresponsealternative54
- name: QueryResponseAlternative55
  property_count: 12
  slug: posthog-queryresponsealternative55
- name: QueryResponseAlternative57
  property_count: 13
  slug: posthog-queryresponsealternative57
- name: QueryResponseAlternative58
  property_count: 8
  slug: posthog-queryresponsealternative58
- name: QueryResponseAlternative59
  property_count: 13
  slug: posthog-queryresponsealternative59
- name: QueryResponseAlternative6
  property_count: 8
  slug: posthog-queryresponsealternative6
- name: QueryResponseAlternative60
  property_count: 11
  slug: posthog-queryresponsealternative60
- name: QueryResponseAlternative62
  property_count: 10
  slug: posthog-queryresponsealternative62
- name: QueryResponseAlternative63
  property_count: 11
  slug: posthog-queryresponsealternative63
- name: QueryResponseAlternative64
  property_count: 11
  slug: posthog-queryresponsealternative64
- name: QueryResponseAlternative65
  property_count: 12
  slug: posthog-queryresponsealternative65
- name: QueryResponseAlternative66
  property_count: 9
  slug: posthog-queryresponsealternative66
- name: QueryResponseAlternative67
  property_count: 7
  slug: posthog-queryresponsealternative67
- name: QueryResponseAlternative68
  property_count: 7
  slug: posthog-queryresponsealternative68
- name: QueryResponseAlternative69
  property_count: 7
  slug: posthog-queryresponsealternative69
- name: QueryResponseAlternative7
  property_count: 4
  slug: posthog-queryresponsealternative7
- name: QueryResponseAlternative70
  property_count: 7
  slug: posthog-queryresponsealternative70
- name: QueryResponseAlternative72
  property_count: 12
  slug: posthog-queryresponsealternative72
- name: QueryResponseAlternative73
  property_count: 2
  slug: posthog-queryresponsealternative73
- name: QueryResponseAlternative74
  property_count: 9
  slug: posthog-queryresponsealternative74
- name: QueryResponseAlternative75
  property_count: 12
  slug: posthog-queryresponsealternative75
- name: QueryResponseAlternative76
  property_count: 8
  slug: posthog-queryresponsealternative76
- name: QueryResponseAlternative77
  property_count: 7
  slug: posthog-queryresponsealternative77
- name: QueryResponseAlternative78
  property_count: 11
  slug: posthog-queryresponsealternative78
- name: QueryResponseAlternative79
  property_count: 1
  slug: posthog-queryresponsealternative79
- name: QueryResponseAlternative8
  property_count: 16
  slug: posthog-queryresponsealternative8
- name: QueryResponseAlternative80
  property_count: 10
  slug: posthog-queryresponsealternative80
- name: QueryResponseAlternative81
  property_count: 10
  slug: posthog-queryresponsealternative81
- name: QueryResponseAlternative82
  property_count: 7
  slug: posthog-queryresponsealternative82
- name: QueryResponseAlternative83
  property_count: 11
  slug: posthog-queryresponsealternative83
- name: QueryResponseAlternative85
  property_count: 5
  slug: posthog-queryresponsealternative85
- name: QueryResponseAlternative86
  property_count: 7
  slug: posthog-queryresponsealternative86
- name: QueryResponseAlternative87
  property_count: 7
  slug: posthog-queryresponsealternative87
- name: QueryResponseAlternative88
  property_count: 7
  slug: posthog-queryresponsealternative88
- name: QueryResponseAlternative89
  property_count: 12
  slug: posthog-queryresponsealternative89
- name: QueryResponseAlternative9
  property_count: 8
  slug: posthog-queryresponsealternative9
- name: QueryResponseAlternative90
  property_count: 7
  slug: posthog-queryresponsealternative90
- name: QueryResponseAlternative91
  property_count: 7
  slug: posthog-queryresponsealternative91
- name: QueryStatus
  property_count: 16
  slug: posthog-querystatus
- name: QueryStatusResponse
  property_count: 1
  slug: posthog-querystatusresponse
- name: QueryTiming
  property_count: 2
  slug: posthog-querytiming
- name: QueryUpgradeRequest
  property_count: 1
  slug: posthog-queryupgraderequest
- name: QueryUpgradeResponse
  property_count: 1
  slug: posthog-queryupgraderesponse
- name: ReasoningEffortEnum
  property_count: 0
  slug: posthog-reasoningeffortenum
- name: RecomputeResult
  property_count: 5
  slug: posthog-recomputeresult
- name: RecordingOrder
  property_count: 0
  slug: posthog-recordingorder
- name: RecordingOrderDirection
  property_count: 0
  slug: posthog-recordingorderdirection
- name: RecordingPropertyFilter
  property_count: 5
  slug: posthog-recordingpropertyfilter
- name: RecordingsQuery
  property_count: 25
  slug: posthog-recordingsquery
- name: RecordingsQueryResponse
  property_count: 9
  slug: posthog-recordingsqueryresponse
- name: RefreshType
  property_count: 0
  slug: posthog-refreshtype
- name: ReorderTilesRequest
  property_count: 1
  slug: posthog-reordertilesrequest
- name: Repo
  property_count: 7
  slug: posthog-repo
- name: RepositoryReadinessResponse
  property_count: 12
  slug: posthog-repositoryreadinessresponse
- name: ResetPasswordResponse
  property_count: 2
  slug: posthog-resetpasswordresponse
- name: ResolvedDateRangeResponse
  property_count: 2
  slug: posthog-resolveddaterangeresponse
- name: Response
  property_count: 13
  slug: posthog-response
- name: Response1
  property_count: 13
  slug: posthog-response1
- name: Response10
  property_count: 12
  slug: posthog-response10
- name: Response11
  property_count: 8
  slug: posthog-response11
- name: Response12
  property_count: 8
  slug: posthog-response12
- name: Response13
  property_count: 8
  slug: posthog-response13
- name: Response14
  property_count: 7
  slug: posthog-response14
- name: Response15
  property_count: 8
  slug: posthog-response15
- name: Response16
  property_count: 12
  slug: posthog-response16
- name: Response18
  property_count: 13
  slug: posthog-response18
- name: Response19
  property_count: 8
  slug: posthog-response19
- name: Response2
  property_count: 13
  slug: posthog-response2
- name: Response20
  property_count: 13
  slug: posthog-response20
- name: Response21
  property_count: 11
  slug: posthog-response21
- name: Response22
  property_count: 11
  slug: posthog-response22
- name: Response23
  property_count: 10
  slug: posthog-response23
- name: Response24
  property_count: 11
  slug: posthog-response24
- name: Response25
  property_count: 11
  slug: posthog-response25
- name: Response26
  property_count: 12
  slug: posthog-response26
- name: Response3
  property_count: 16
  slug: posthog-response3
- name: Response4
  property_count: 11
  slug: posthog-response4
- name: Response5
  property_count: 14
  slug: posthog-response5
- name: Response6
  property_count: 13
  slug: posthog-response6
- name: Response8
  property_count: 7
  slug: posthog-response8
- name: Response9
  property_count: 12
  slug: posthog-response9
- name: ResponseSamplingIntervalTypeEnum
  property_count: 0
  slug: posthog-responsesamplingintervaltypeenum
- name: RestrictionLevelEnum
  property_count: 0
  slug: posthog-restrictionlevelenum
- name: ResultCustomizationBy
  property_count: 0
  slug: posthog-resultcustomizationby
- name: ResultCustomizationByPosition
  property_count: 3
  slug: posthog-resultcustomizationbyposition
- name: ResultCustomizationByValue
  property_count: 3
  slug: posthog-resultcustomizationbyvalue
- name: Results
  property_count: 2
  slug: posthog-results
- name: RETENTION
  property_count: 3
  slug: posthog-retention
- name: RetentionDashboardDisplayType
  property_count: 0
  slug: posthog-retentiondashboarddisplaytype
- name: RetentionEntity
  property_count: 11
  slug: posthog-retentionentity
- name: RetentionEntityKind
  property_count: 0
  slug: posthog-retentionentitykind
- name: RetentionFilter
  property_count: 20
  slug: posthog-retentionfilter
- name: RetentionPeriod
  property_count: 0
  slug: posthog-retentionperiod
- name: RetentionQuery
  property_count: 13
  slug: posthog-retentionquery
- name: RetentionQueryResponse
  property_count: 7
  slug: posthog-retentionqueryresponse
- name: RetentionReference
  property_count: 0
  slug: posthog-retentionreference
- name: RetentionResult
  property_count: 4
  slug: posthog-retentionresult
- name: RetentionType
  property_count: 0
  slug: posthog-retentiontype
- name: RetentionValue
  property_count: 3
  slug: posthog-retentionvalue
- name: RevenueAnalyticsBreakdown
  property_count: 2
  slug: posthog-revenueanalyticsbreakdown
- name: RevenueAnalyticsGrossRevenueQuery
  property_count: 9
  slug: posthog-revenueanalyticsgrossrevenuequery
- name: RevenueAnalyticsGrossRevenueQueryResponse
  property_count: 8
  slug: posthog-revenueanalyticsgrossrevenuequeryresponse
- name: RevenueAnalyticsMetricsQuery
  property_count: 9
  slug: posthog-revenueanalyticsmetricsquery
- name: RevenueAnalyticsMetricsQueryResponse
  property_count: 8
  slug: posthog-revenueanalyticsmetricsqueryresponse
- name: RevenueAnalyticsMRRQuery
  property_count: 9
  slug: posthog-revenueanalyticsmrrquery
- name: RevenueAnalyticsMRRQueryResponse
  property_count: 8
  slug: posthog-revenueanalyticsmrrqueryresponse
- name: RevenueAnalyticsMRRQueryResultItem
  property_count: 5
  slug: posthog-revenueanalyticsmrrqueryresultitem
- name: RevenueAnalyticsOverviewItem
  property_count: 2
  slug: posthog-revenueanalyticsoverviewitem
- name: RevenueAnalyticsOverviewItemKey
  property_count: 0
  slug: posthog-revenueanalyticsoverviewitemkey
- name: RevenueAnalyticsOverviewQuery
  property_count: 7
  slug: posthog-revenueanalyticsoverviewquery
- name: RevenueAnalyticsOverviewQueryResponse
  property_count: 7
  slug: posthog-revenueanalyticsoverviewqueryresponse
- name: RevenueAnalyticsPropertyFilter
  property_count: 5
  slug: posthog-revenueanalyticspropertyfilter
- name: RevenueAnalyticsTopCustomersGroupBy
  property_count: 0
  slug: posthog-revenueanalyticstopcustomersgroupby
- name: RevenueAnalyticsTopCustomersQuery
  property_count: 8
  slug: posthog-revenueanalyticstopcustomersquery
- name: RevenueAnalyticsTopCustomersQueryResponse
  property_count: 8
  slug: posthog-revenueanalyticstopcustomersqueryresponse
- name: RevenueCurrencyPropertyConfig
  property_count: 2
  slug: posthog-revenuecurrencypropertyconfig
- name: RevenueExampleDataWarehouseTablesQuery
  property_count: 7
  slug: posthog-revenueexampledatawarehousetablesquery
- name: RevenueExampleDataWarehouseTablesQueryResponse
  property_count: 12
  slug: posthog-revenueexampledatawarehousetablesqueryresponse
- name: RevenueExampleEventsQuery
  property_count: 7
  slug: posthog-revenueexampleeventsquery
- name: RevenueExampleEventsQueryResponse
  property_count: 12
  slug: posthog-revenueexampleeventsqueryresponse
- name: ReviewQueue
  property_count: 7
  slug: posthog-reviewqueue
- name: ReviewQueueCreate
  property_count: 1
  slug: posthog-reviewqueuecreate
- name: ReviewQueueItem
  property_count: 8
  slug: posthog-reviewqueueitem
- name: ReviewQueueItemCreate
  property_count: 2
  slug: posthog-reviewqueueitemcreate
- name: ReviewStateCounts
  property_count: 4
  slug: posthog-reviewstatecounts
- name: Role
  property_count: 6
  slug: posthog-role
- name: RoleAtOrganizationEnum
  property_count: 0
  slug: posthog-roleatorganizationenum
- name: RoleExternalReference
  property_count: 9
  slug: posthog-roleexternalreference
- name: RoleLookupResponse
  property_count: 1
  slug: posthog-rolelookupresponse
- name: RoleMembership
  property_count: 7
  slug: posthog-rolemembership
- name: RuleTypeEnum
  property_count: 0
  slug: posthog-ruletypeenum
- name: Run
  property_count: 17
  slug: posthog-run
- name: RunInsightsResponse
  property_count: 1
  slug: posthog-runinsightsresponse
- name: RunSourceEnum
  property_count: 0
  slug: posthog-runsourceenum
- name: RunSummary
  property_count: 7
  slug: posthog-runsummary
- name: RuntimeAdapterEnum
  property_count: 0
  slug: posthog-runtimeadapterenum
- name: S3PresignedPost
  property_count: 2
  slug: posthog-s3presignedpost
- name: SampleRatioMismatch
  property_count: 2
  slug: posthog-sampleratiomismatch
- name: SamplingRate
  property_count: 2
  slug: posthog-samplingrate
- name: SandboxEnvironment
  property_count: 14
  slug: posthog-sandboxenvironment
- name: SandboxEnvironmentList
  property_count: 10
  slug: posthog-sandboxenvironmentlist
- name: SavedInsightNode
  property_count: 44
  slug: posthog-savedinsightnode
- name: SavedQueryStatusEnum
  property_count: 0
  slug: posthog-savedquerystatusenum
- name: Scale
  property_count: 0
  slug: posthog-scale
- name: ScanEvidence
  property_count: 6
  slug: posthog-scanevidence
- name: ScenePersonalisationBasic
  property_count: 2
  slug: posthog-scenepersonalisationbasic
- name: ScheduleEnum
  property_count: 0
  slug: posthog-scheduleenum
- name: SchemaPropertyGroup
  property_count: 8
  slug: posthog-schemapropertygroup
- name: SchemaPropertyGroupProperty
  property_count: 8
  slug: posthog-schemapropertygroupproperty
- name: SchemaPropertyGroupPropertyPropertyTypeEnum
  property_count: 0
  slug: posthog-schemapropertygrouppropertypropertytypeenum
- name: ScoreDefinition
  property_count: 11
  slug: posthog-scoredefinition
- name: ScoreDefinitionConfig
  property_count: 0
  slug: posthog-scoredefinitionconfig
- name: ScoreDefinitionCreate
  property_count: 5
  slug: posthog-scoredefinitioncreate
- name: ScoreDefinitionNewVersion
  property_count: 1
  slug: posthog-scoredefinitionnewversion
- name: SdkAssessment
  property_count: 11
  slug: posthog-sdkassessment
- name: SdkAssessmentSeverityEnum
  property_count: 0
  slug: posthog-sdkassessmentseverityenum
- name: SdkHealthReport
  property_count: 5
  slug: posthog-sdkhealthreport
- name: SdkReleaseAssessment
  property_count: 13
  slug: posthog-sdkreleaseassessment
- name: SelectionModeEnum
  property_count: 0
  slug: posthog-selectionmodeenum
- name: SentimentBatchResponse
  property_count: 1
  slug: posthog-sentimentbatchresponse
- name: SentimentRequest
  property_count: 5
  slug: posthog-sentimentrequest
- name: SentimentRequestAnalysisLevelEnum
  property_count: 0
  slug: posthog-sentimentrequestanalysislevelenum
- name: SentimentResult
  property_count: 5
  slug: posthog-sentimentresult
- name: Series
  property_count: 2
  slug: posthog-series
- name: SessionAttributionExplorerQuery
  property_count: 9
  slug: posthog-sessionattributionexplorerquery
- name: SessionAttributionExplorerQueryResponse
  property_count: 12
  slug: posthog-sessionattributionexplorerqueryresponse
- name: SessionAttributionGroupBy
  property_count: 0
  slug: posthog-sessionattributiongroupby
- name: SessionData
  property_count: 4
  slug: posthog-sessiondata
- name: SessionGroupSummary
  property_count: 9
  slug: posthog-sessiongroupsummary
- name: SessionGroupSummaryMinimal
  property_count: 5
  slug: posthog-sessiongroupsummaryminimal
- name: SessionPropertyFilter
  property_count: 5
  slug: posthog-sessionpropertyfilter
- name: SessionRecording
  property_count: 27
  slug: posthog-sessionrecording
- name: SessionRecordingExternalReference
  property_count: 6
  slug: posthog-sessionrecordingexternalreference
- name: SessionRecordingPlaylist
  property_count: 16
  slug: posthog-sessionrecordingplaylist
- name: SessionRecordingPlaylistTypeEnum
  property_count: 0
  slug: posthog-sessionrecordingplaylisttypeenum
- name: SessionRecordingRetentionPeriodEnum
  property_count: 0
  slug: posthog-sessionrecordingretentionperiodenum
- name: SessionRecordingType
  property_count: 30
  slug: posthog-sessionrecordingtype
- name: SessionsQuery
  property_count: 19
  slug: posthog-sessionsquery
- name: SessionsQueryResponse
  property_count: 12
  slug: posthog-sessionsqueryresponse
- name: SessionsTimelineQuery
  property_count: 8
  slug: posthog-sessionstimelinequery
- name: SessionsTimelineQueryResponse
  property_count: 8
  slug: posthog-sessionstimelinequeryresponse
- name: SessionSummaries
  property_count: 2
  slug: posthog-sessionsummaries
- name: SessionSummariesConfig
  property_count: 1
  slug: posthog-sessionsummariesconfig
- name: SessionsV2JoinMode
  property_count: 0
  slug: posthog-sessionsv2joinmode
- name: SessionTableVersion
  property_count: 0
  slug: posthog-sessiontableversion
- name: Settings
  property_count: 2
  slug: posthog-settings
- name: SeverityLevelsEnum
  property_count: 0
  slug: posthog-severitylevelsenum
- name: SharePassword
  property_count: 5
  slug: posthog-sharepassword
- name: SharingConfiguration
  property_count: 6
  slug: posthog-sharingconfiguration
- name: ShipVariant
  property_count: 3
  slug: posthog-shipvariant
- name: ShortcutPositionEnum
  property_count: 0
  slug: posthog-shortcutpositionenum
- name: SignalReport
  property_count: 16
  slug: posthog-signalreport
- name: SignalReportStatusEnum
  property_count: 0
  slug: posthog-signalreportstatusenum
- name: SignalReportTaskRelationshipEnum
  property_count: 0
  slug: posthog-signalreporttaskrelationshipenum
- name: SignalSourceConfig
  property_count: 8
  slug: posthog-signalsourceconfig
- name: SignalSourceConfigSourceTypeEnum
  property_count: 0
  slug: posthog-signalsourceconfigsourcetypeenum
- name: SignalUserAutonomyConfig
  property_count: 5
  slug: posthog-signaluserautonomyconfig
- name: SimilarIssue
  property_count: 7
  slug: posthog-similarissue
- name: SimpleExternalDataSourceSerializers
  property_count: 5
  slug: posthog-simpleexternaldatasourceserializers
- name: SimpleIntervalType
  property_count: 0
  slug: posthog-simpleintervaltype
- name: SlackChannel
  property_count: 6
  slug: posthog-slackchannel
- name: SlackChannelsResponse
  property_count: 2
  slug: posthog-slackchannelsresponse
- name: Snapshot
  property_count: 16
  slug: posthog-snapshot
- name: SnapshotHistoryEntry
  property_count: 10
  slug: posthog-snapshothistoryentry
- name: SnapshotManifestItem
  property_count: 5
  slug: posthog-snapshotmanifestitem
- name: SnapshotSource
  property_count: 0
  slug: posthog-snapshotsource
- name: SourceProductEnum
  property_count: 0
  slug: posthog-sourceproductenum
- name: SpanPropertyFilter
  property_count: 5
  slug: posthog-spanpropertyfilter
- name: SpanPropertyFilterType
  property_count: 0
  slug: posthog-spanpropertyfiltertype
- name: SparklineBreakdownByEnum
  property_count: 0
  slug: posthog-sparklinebreakdownbyenum
- name: StageEnum
  property_count: 0
  slug: posthog-stageenum
- name: StartHandling
  property_count: 0
  slug: posthog-starthandling
- name: StaticFilters
  property_count: 4
  slug: posthog-staticfilters
- name: StatusItem
  property_count: 2
  slug: posthog-statusitem
- name: StatusReasonEnum
  property_count: 0
  slug: posthog-statusreasonenum
- name: StepOrderValue
  property_count: 0
  slug: posthog-stepordervalue
- name: StickinessActorsQuery
  property_count: 11
  slug: posthog-stickinessactorsquery
- name: StickinessComputationMode
  property_count: 0
  slug: posthog-stickinesscomputationmode
- name: StickinessCriteria
  property_count: 2
  slug: posthog-stickinesscriteria
- name: StickinessFilter
  property_count: 9
  slug: posthog-stickinessfilter
- name: StickinessOperator
  property_count: 0
  slug: posthog-stickinessoperator
- name: StickinessQuery
  property_count: 15
  slug: posthog-stickinessquery
- name: StickinessQueryResponse
  property_count: 7
  slug: posthog-stickinessqueryresponse
- name: StringMatchOperatorEnum
  property_count: 0
  slug: posthog-stringmatchoperatorenum
- name: StringPropertyFilter
  property_count: 4
  slug: posthog-stringpropertyfilter
- name: StructuredSummary
  property_count: 4
  slug: posthog-structuredsummary
- name: Style
  property_count: 0
  slug: posthog-style
- name: Subscription
  property_count: 25
  slug: posthog-subscription
- name: SubscriptionDelivery
  property_count: 17
  slug: posthog-subscriptiondelivery
- name: SubscriptionDeliveryStatusEnum
  property_count: 0
  slug: posthog-subscriptiondeliverystatusenum
- name: SubscriptionFrequencyEnum
  property_count: 0
  slug: posthog-subscriptionfrequencyenum
- name: SuggestedQuestionsQuery
  property_count: 5
  slug: posthog-suggestedquestionsquery
- name: SuggestedQuestionsQueryResponse
  property_count: 1
  slug: posthog-suggestedquestionsqueryresponse
- name: SuggestReplyError
  property_count: 2
  slug: posthog-suggestreplyerror
- name: SuggestReplyResponse
  property_count: 1
  slug: posthog-suggestreplyresponse
- name: SummarizeRequest
  property_count: 9
  slug: posthog-summarizerequest
- name: SummarizeResponse
  property_count: 3
  slug: posthog-summarizeresponse
- name: SummarizeTypeEnum
  property_count: 0
  slug: posthog-summarizetypeenum
- name: SummaryBullet
  property_count: 2
  slug: posthog-summarybullet
- name: SummaryOutcome
  property_count: 2
  slug: posthog-summaryoutcome
- name: Survey
  property_count: 35
  slug: posthog-survey
- name: SurveyAppearanceSchema
  property_count: 29
  slug: posthog-surveyappearanceschema
- name: SurveyBranchingSchema
  property_count: 0
  slug: posthog-surveybranchingschema
- name: SurveyConditionEventValueSchema
  property_count: 1
  slug: posthog-surveyconditioneventvalueschema
- name: SurveyConditionsSchema
  property_count: 8
  slug: posthog-surveyconditionsschema
- name: SurveyEndBranching
  property_count: 1
  slug: posthog-surveyendbranching
- name: SurveyEndBranchingTypeEnum
  property_count: 0
  slug: posthog-surveyendbranchingtypeenum
- name: SurveyEventsConditionSchema
  property_count: 2
  slug: posthog-surveyeventsconditionschema
- name: SurveyGlobalStatsResponse
  property_count: 2
  slug: posthog-surveyglobalstatsresponse
- name: SurveyLinkQuestionSchema
  property_count: 7
  slug: posthog-surveylinkquestionschema
- name: SurveyLinkQuestionSchemaTypeEnum
  property_count: 0
  slug: posthog-surveylinkquestionschematypeenum
- name: SurveyMultipleChoiceQuestionSchema
  property_count: 9
  slug: posthog-surveymultiplechoicequestionschema
- name: SurveyMultipleChoiceQuestionSchemaTypeEnum
  property_count: 0
  slug: posthog-surveymultiplechoicequestionschematypeenum
- name: SurveyNextQuestionBranching
  property_count: 1
  slug: posthog-surveynextquestionbranching
- name: SurveyNextQuestionBranchingTypeEnum
  property_count: 0
  slug: posthog-surveynextquestionbranchingtypeenum
- name: SurveyOpenQuestionSchema
  property_count: 6
  slug: posthog-surveyopenquestionschema
- name: SurveyOpenQuestionSchemaTypeEnum
  property_count: 0
  slug: posthog-surveyopenquestionschematypeenum
- name: SurveyQuestionInputSchema
  property_count: 0
  slug: posthog-surveyquestioninputschema
- name: SurveyRatingQuestionSchema
  property_count: 11
  slug: posthog-surveyratingquestionschema
- name: SurveyRatingQuestionSchemaDisplayEnum
  property_count: 0
  slug: posthog-surveyratingquestionschemadisplayenum
- name: SurveyRatingQuestionSchemaTypeEnum
  property_count: 0
  slug: posthog-surveyratingquestionschematypeenum
- name: SurveyResponseBasedBranching
  property_count: 2
  slug: posthog-surveyresponsebasedbranching
- name: SurveyResponseBasedBranchingTypeEnum
  property_count: 0
  slug: posthog-surveyresponsebasedbranchingtypeenum
- name: SurveySerializerCreateUpdateOnly
  property_count: 37
  slug: posthog-surveyserializercreateupdateonly
- name: SurveySerializerCreateUpdateOnlySchema
  property_count: 37
  slug: posthog-surveyserializercreateupdateonlyschema
- name: SurveySingleChoiceQuestionSchema
  property_count: 10
  slug: posthog-surveysinglechoicequestionschema
- name: SurveySingleChoiceQuestionSchemaTypeEnum
  property_count: 0
  slug: posthog-surveysinglechoicequestionschematypeenum
- name: SurveySpecificQuestionBranching
  property_count: 2
  slug: posthog-surveyspecificquestionbranching
- name: SurveySpecificQuestionBranchingTypeEnum
  property_count: 0
  slug: posthog-surveyspecificquestionbranchingtypeenum
- name: SurveyStatsResponse
  property_count: 5
  slug: posthog-surveystatsresponse
- name: SurveyType
  property_count: 0
  slug: posthog-surveytype
- name: _SymbolSetDownloadResponse
  property_count: 1
  slug: posthog-symbolsetdownloadresponse
- name: SyncFrequencyEnum
  property_count: 0
  slug: posthog-syncfrequencyenum
- name: SyncTypeEnum
  property_count: 0
  slug: posthog-synctypeenum
- name: Table
  property_count: 13
  slug: posthog-table
- name: TableFormatEnum
  property_count: 0
  slug: posthog-tableformatenum
- name: TableSettings
  property_count: 4
  slug: posthog-tablesettings
- name: Tagger
  property_count: 12
  slug: posthog-tagger
- name: TaggerCondition
  property_count: 3
  slug: posthog-taggercondition
- name: TaggerModelConfiguration
  property_count: 4
  slug: posthog-taggermodelconfiguration
- name: TaggerTypeEnum
  property_count: 0
  slug: posthog-taggertypeenum
- name: TargetTypeEnum
  property_count: 0
  slug: posthog-targettypeenum
- name: Task
  property_count: 19
  slug: posthog-task
- name: TaskAutomation
  property_count: 16
  slug: posthog-taskautomation
- name: TaskExecutionModeEnum
  property_count: 0
  slug: posthog-taskexecutionmodeenum
- name: TaskRepositoriesResponse
  property_count: 1
  slug: posthog-taskrepositoriesresponse
- name: TaskRunAppendLogRequest
  property_count: 1
  slug: posthog-taskrunappendlogrequest
- name: TaskRunArtifactFinalizeUpload
  property_count: 6
  slug: posthog-taskrunartifactfinalizeupload
- name: TaskRunArtifactPrepareUpload
  property_count: 5
  slug: posthog-taskrunartifactprepareupload
- name: TaskRunArtifactPrepareUploadResponse
  property_count: 9
  slug: posthog-taskrunartifactprepareuploadresponse
- name: TaskRunArtifactPresignRequest
  property_count: 1
  slug: posthog-taskrunartifactpresignrequest
- name: TaskRunArtifactPresignResponse
  property_count: 2
  slug: posthog-taskrunartifactpresignresponse
- name: TaskRunArtifactResponse
  property_count: 8
  slug: posthog-taskrunartifactresponse
- name: TaskRunArtifactsFinalizeUploadRequest
  property_count: 1
  slug: posthog-taskrunartifactsfinalizeuploadrequest
- name: TaskRunArtifactsFinalizeUploadResponse
  property_count: 1
  slug: posthog-taskrunartifactsfinalizeuploadresponse
- name: TaskRunArtifactsPrepareUploadRequest
  property_count: 1
  slug: posthog-taskrunartifactsprepareuploadrequest
- name: TaskRunArtifactsPrepareUploadResponse
  property_count: 1
  slug: posthog-taskrunartifactsprepareuploadresponse
- name: TaskRunArtifactsUploadRequest
  property_count: 1
  slug: posthog-taskrunartifactsuploadrequest
- name: TaskRunArtifactsUploadResponse
  property_count: 1
  slug: posthog-taskrunartifactsuploadresponse
- name: TaskRunArtifactTypeEnum
  property_count: 0
  slug: posthog-taskrunartifacttypeenum
- name: TaskRunArtifactUpload
  property_count: 6
  slug: posthog-taskrunartifactupload
- name: TaskRunBootstrapCreateRequest
  property_count: 12
  slug: posthog-taskrunbootstrapcreaterequest
- name: TaskRunBootstrapCreateRequestEnvironmentEnum
  property_count: 0
  slug: posthog-taskrunbootstrapcreaterequestenvironmentenum
- name: TaskRunBootstrapCreateRequestInitialPermissionModeEnum
  property_count: 0
  slug: posthog-taskrunbootstrapcreaterequestinitialpermissionmodeenum
- name: TaskRunCommandRequest
  property_count: 4
  slug: posthog-taskruncommandrequest
- name: TaskRunCommandResponse
  property_count: 4
  slug: posthog-taskruncommandresponse
- name: TaskRunCreateRequestSchema
  property_count: 0
  slug: posthog-taskruncreaterequestschema
- name: TaskRunDetail
  property_count: 18
  slug: posthog-taskrundetail
- name: TaskRunDetailEnvironmentEnum
  property_count: 0
  slug: posthog-taskrundetailenvironmentenum
- name: TaskRunDetailProviderEnum
  property_count: 0
  slug: posthog-taskrundetailproviderenum
- name: TaskRunDetailStatusEnum
  property_count: 0
  slug: posthog-taskrundetailstatusenum
- name: TaskRunErrorResponse
  property_count: 6
  slug: posthog-taskrunerrorresponse
- name: TaskRunRelayMessageRequest
  property_count: 1
  slug: posthog-taskrunrelaymessagerequest
- name: TaskRunRelayMessageResponse
  property_count: 2
  slug: posthog-taskrunrelaymessageresponse
- name: TaskRunResumeRequestSchema
  property_count: 9
  slug: posthog-taskrunresumerequestschema
- name: TaskRunStartRequest
  property_count: 2
  slug: posthog-taskrunstartrequest
- name: TaskRunUpdateEnvironmentEnum
  property_count: 0
  slug: posthog-taskrunupdateenvironmentenum
- name: TaskRunUpdateStatusEnum
  property_count: 0
  slug: posthog-taskrunupdatestatusenum
- name: TaskStagedArtifactFinalizeUpload
  property_count: 6
  slug: posthog-taskstagedartifactfinalizeupload
- name: TaskStagedArtifactPrepareUpload
  property_count: 5
  slug: posthog-taskstagedartifactprepareupload
- name: TaskStagedArtifactPrepareUploadResponse
  property_count: 9
  slug: posthog-taskstagedartifactprepareuploadresponse
- name: TaskStagedArtifactsFinalizeUploadRequest
  property_count: 1
  slug: posthog-taskstagedartifactsfinalizeuploadrequest
- name: TaskStagedArtifactsFinalizeUploadResponse
  property_count: 1
  slug: posthog-taskstagedartifactsfinalizeuploadresponse
- name: TaskStagedArtifactsPrepareUploadRequest
  property_count: 1
  slug: posthog-taskstagedartifactsprepareuploadrequest
- name: TaskStagedArtifactsPrepareUploadResponse
  property_count: 1
  slug: posthog-taskstagedartifactsprepareuploadresponse
- name: TaxonomicFilterGroupType
  property_count: 0
  slug: posthog-taxonomicfiltergrouptype
- name: Team
  property_count: 85
  slug: posthog-team
- name: TeamBasic
  property_count: 12
  slug: posthog-teambasic
- name: TeamCustomerAnalyticsConfig
  property_count: 5
  slug: posthog-teamcustomeranalyticsconfig
- name: TeamMarketingAnalyticsConfig
  property_count: 7
  slug: posthog-teammarketinganalyticsconfig
- name: TeamRevenueAnalyticsConfig
  property_count: 4
  slug: posthog-teamrevenueanalyticsconfig
- name: TeamTaxonomyItem
  property_count: 2
  slug: posthog-teamtaxonomyitem
- name: TeamTaxonomyQuery
  property_count: 7
  slug: posthog-teamtaxonomyquery
- name: TeamTaxonomyQueryResponse
  property_count: 10
  slug: posthog-teamtaxonomyqueryresponse
- name: TestHogRequest
  property_count: 4
  slug: posthog-testhogrequest
- name: TestHogResponse
  property_count: 2
  slug: posthog-testhogresponse
- name: TestHogResultItem
  property_count: 7
  slug: posthog-testhogresultitem
- name: TextMatching
  property_count: 0
  slug: posthog-textmatching
- name: TextReprMetadata
  property_count: 7
  slug: posthog-textreprmetadata
- name: TextReprOptions
  property_count: 10
  slug: posthog-textreproptions
- name: TextReprRequest
  property_count: 3
  slug: posthog-textreprrequest
- name: TextReprResponse
  property_count: 2
  slug: posthog-textreprresponse
- name: ThemeModeEnum
  property_count: 0
  slug: posthog-thememodeenum
- name: Threshold
  property_count: 4
  slug: posthog-threshold
- name: ThresholdDetectorConfig
  property_count: 4
  slug: posthog-thresholddetectorconfig
- name: ThresholdOperatorEnum
  property_count: 0
  slug: posthog-thresholdoperatorenum
- name: ThresholdWithAlert
  property_count: 5
  slug: posthog-thresholdwithalert
- name: Ticket
  property_count: 31
  slug: posthog-ticket
- name: TicketAssignment
  property_count: 4
  slug: posthog-ticketassignment
- name: TicketPerson
  property_count: 6
  slug: posthog-ticketperson
- name: TicketStatusEnum
  property_count: 0
  slug: posthog-ticketstatusenum
- name: TicketView
  property_count: 6
  slug: posthog-ticketview
- name: TimelineEntry
  property_count: 3
  slug: posthog-timelineentry
- name: TimeWindowMode
  property_count: 0
  slug: posthog-timewindowmode
- name: TimezoneEnum
  property_count: 0
  slug: posthog-timezoneenum
- name: ToleratedHashEntry
  property_count: 7
  slug: posthog-toleratedhashentry
- name: ToolApprovalUpdateApprovalStateEnum
  property_count: 0
  slug: posthog-toolapprovalupdateapprovalstateenum
- name: ToolbarModeEnum
  property_count: 0
  slug: posthog-toolbarmodeenum
- name: TopPage
  property_count: 4
  slug: posthog-toppage
- name: TopSource
  property_count: 3
  slug: posthog-topsource
- name: TraceNeighborsQuery
  property_count: 11
  slug: posthog-traceneighborsquery
- name: TraceNeighborsQueryResponse
  property_count: 5
  slug: posthog-traceneighborsqueryresponse
- name: TraceQuery
  property_count: 8
  slug: posthog-tracequery
- name: TraceQueryResponse
  property_count: 11
  slug: posthog-tracequeryresponse
- name: TraceReview
  property_count: 9
  slug: posthog-tracereview
- name: TraceReviewCreate
  property_count: 4
  slug: posthog-tracereviewcreate
- name: TraceReviewScore
  property_count: 13
  slug: posthog-tracereviewscore
- name: TraceReviewScoreWrite
  property_count: 5
  slug: posthog-tracereviewscorewrite
- name: TraceSpansQuery
  property_count: 16
  slug: posthog-tracespansquery
- name: TraceSpansQueryResponse
  property_count: 11
  slug: posthog-tracespansqueryresponse
- name: TracesQuery
  property_count: 16
  slug: posthog-tracesquery
- name: TracesQueryResponse
  property_count: 11
  slug: posthog-tracesqueryresponse
- name: TranscriptSegment
  property_count: 5
  slug: posthog-transcriptsegment
- name: TranslateRequest
  property_count: 2
  slug: posthog-translaterequest
- name: TrendsAlertConfig
  property_count: 3
  slug: posthog-trendsalertconfig
- name: TrendsFilter
  property_count: 30
  slug: posthog-trendsfilter
- name: TrendsFormulaNode
  property_count: 2
  slug: posthog-trendsformulanode
- name: TrendsQuery
  property_count: 17
  slug: posthog-trendsquery
- name: TrendsQueryResponse
  property_count: 9
  slug: posthog-trendsqueryresponse
- name: Trigger
  property_count: 3
  slug: posthog-trigger
- name: UploadTarget
  property_count: 3
  slug: posthog-uploadtarget
- name: UrlMatching
  property_count: 0
  slug: posthog-urlmatching
- name: UsageMetric
  property_count: 10
  slug: posthog-usagemetric
- name: UsageMetricDisplay
  property_count: 0
  slug: posthog-usagemetricdisplay
- name: UsageMetricFormat
  property_count: 0
  slug: posthog-usagemetricformat
- name: UsageMetricsQuery
  property_count: 8
  slug: posthog-usagemetricsquery
- name: UsageMetricsQueryResponse
  property_count: 7
  slug: posthog-usagemetricsqueryresponse
- name: User
  property_count: 40
  slug: posthog-user
- name: UserBasic
  property_count: 9
  slug: posthog-userbasic
- name: UserBasicInfo
  property_count: 3
  slug: posthog-userbasicinfo
- name: UserBasicType
  property_count: 9
  slug: posthog-userbasictype
- name: UserBlastRadiusRequest
  property_count: 2
  slug: posthog-userblastradiusrequest
- name: UserBlastRadiusResponse
  property_count: 2
  slug: posthog-userblastradiusresponse
- name: UserGitHubAccount
  property_count: 2
  slug: posthog-usergithubaccount
- name: UserGitHubIntegrationItem
  property_count: 7
  slug: posthog-usergithubintegrationitem
- name: UserGitHubIntegrationListResponse
  property_count: 1
  slug: posthog-usergithubintegrationlistresponse
- name: UserGitHubLinkStartRequest
  property_count: 2
  slug: posthog-usergithublinkstartrequest
- name: UserGitHubLinkStartResponse
  property_count: 2
  slug: posthog-usergithublinkstartresponse
- name: UserInterview
  property_count: 7
  slug: posthog-userinterview
- name: ValidationStatusEnum
  property_count: 0
  slug: posthog-validationstatusenum
- name: VectorSearchQuery
  property_count: 7
  slug: posthog-vectorsearchquery
- name: VectorSearchQueryResponse
  property_count: 7
  slug: posthog-vectorsearchqueryresponse
- name: VectorSearchResponseItem
  property_count: 2
  slug: posthog-vectorsearchresponseitem
- name: ViewLink
  property_count: 10
  slug: posthog-viewlink
- name: ViewLinkValidation
  property_count: 4
  slug: posthog-viewlinkvalidation
- name: VizSpecificOptions
  property_count: 2
  slug: posthog-vizspecificoptions
- name: VolumeBucket
  property_count: 2
  slug: posthog-volumebucket
- name: WarehouseStatusResponse
  property_count: 5
  slug: posthog-warehousestatusresponse
- name: WarehouseStatusResponseStateEnum
  property_count: 0
  slug: posthog-warehousestatusresponsestateenum
- name: WebAnalyticsExternalSummaryQuery
  property_count: 5
  slug: posthog-webanalyticsexternalsummaryquery
- name: WebAnalyticsExternalSummaryQueryResponse
  property_count: 3
  slug: posthog-webanalyticsexternalsummaryqueryresponse
- name: WebAnalyticsItemKind
  property_count: 0
  slug: posthog-webanalyticsitemkind
- name: WebAnalyticsOrderByDirection
  property_count: 0
  slug: posthog-webanalyticsorderbydirection
- name: WebAnalyticsOrderByFields
  property_count: 0
  slug: posthog-webanalyticsorderbyfields
- name: WebAnalyticsSampling
  property_count: 2
  slug: posthog-webanalyticssampling
- name: WebExperimentsAPI
  property_count: 5
  slug: posthog-webexperimentsapi
- name: WebExternalClicksTableQuery
  property_count: 21
  slug: posthog-webexternalclickstablequery
- name: WebExternalClicksTableQueryResponse
  property_count: 13
  slug: posthog-webexternalclickstablequeryresponse
- name: WebGoalsQuery
  property_count: 20
  slug: posthog-webgoalsquery
- name: WebGoalsQueryResponse
  property_count: 13
  slug: posthog-webgoalsqueryresponse
- name: WebNotableChangeItem
  property_count: 7
  slug: posthog-webnotablechangeitem
- name: WebNotableChangesQuery
  property_count: 20
  slug: posthog-webnotablechangesquery
- name: WebNotableChangesQueryResponse
  property_count: 9
  slug: posthog-webnotablechangesqueryresponse
- name: WebOverviewItem
  property_count: 7
  slug: posthog-weboverviewitem
- name: WebOverviewQuery
  property_count: 19
  slug: posthog-weboverviewquery
- name: WebOverviewQueryResponse
  property_count: 11
  slug: posthog-weboverviewqueryresponse
- name: WebPageURLSearchQuery
  property_count: 22
  slug: posthog-webpageurlsearchquery
- name: WebPageURLSearchQueryResponse
  property_count: 9
  slug: posthog-webpageurlsearchqueryresponse
- name: WebStatsBreakdown
  property_count: 0
  slug: posthog-webstatsbreakdown
- name: WebStatsTableQuery
  property_count: 26
  slug: posthog-webstatstablequery
- name: WebStatsTableQueryResponse
  property_count: 14
  slug: posthog-webstatstablequeryresponse
- name: WebTrendsItem
  property_count: 2
  slug: posthog-webtrendsitem
- name: WebTrendsMetric
  property_count: 0
  slug: posthog-webtrendsmetric
- name: WebTrendsQuery
  property_count: 22
  slug: posthog-webtrendsquery
- name: WebTrendsQueryResponse
  property_count: 18
  slug: posthog-webtrendsqueryresponse
- name: WebVitalsMetric
  property_count: 0
  slug: posthog-webvitalsmetric
- name: WebVitalsPathBreakdownQuery
  property_count: 22
  slug: posthog-webvitalspathbreakdownquery
- name: WebVitalsPathBreakdownQueryResponse
  property_count: 7
  slug: posthog-webvitalspathbreakdownqueryresponse
- name: WebVitalsPathBreakdownResult
  property_count: 3
  slug: posthog-webvitalspathbreakdownresult
- name: WebVitalsPathBreakdownResultItem
  property_count: 2
  slug: posthog-webvitalspathbreakdownresultitem
- name: WebVitalsPercentile
  property_count: 0
  slug: posthog-webvitalspercentile
- name: WebVitalsQuery
  property_count: 20
  slug: posthog-webvitalsquery
- name: WeeklyDigestResponse
  property_count: 9
  slug: posthog-weeklydigestresponse
- name: WeekStartDayEnum
  property_count: 0
  slug: posthog-weekstartdayenum
- name: _WelcomeInviter
  property_count: 2
  slug: posthog-welcomeinviter
- name: _WelcomePopularDashboard
  property_count: 5
  slug: posthog-welcomepopulardashboard
- name: _WelcomeRecentActivity
  property_count: 5
  slug: posthog-welcomerecentactivity
- name: WelcomeResponse
  property_count: 8
  slug: posthog-welcomeresponse
- name: _WelcomeSuggestedStep
  property_count: 5
  slug: posthog-welcomesuggestedstep
- name: _WelcomeTeamMember
  property_count: 5
  slug: posthog-welcometeammember
- name: WidgetTypeEnum
  property_count: 0
  slug: posthog-widgettypeenum
- name: WorkflowVariablePropertyFilter
  property_count: 5
  slug: posthog-workflowvariablepropertyfilter
- name: WoWChange
  property_count: 5
  slug: posthog-wowchange
- name: YAxisPosition
  property_count: 0
  slug: posthog-yaxisposition
- name: YAxisScaleType
  property_count: 0
  slug: posthog-yaxisscaletype
- name: YAxisSettings
  property_count: 4
  slug: posthog-yaxissettings
- name: ZScoreDetectorConfig
  property_count: 4
  slug: posthog-zscoredetectorconfig
json_structures:
- name: Posthog Structure
  property_count: 0
  slug: posthog-structure
layout: provider
modified: '2026-05-30'
name: PostHog
nav: Providers
network: true
overview: 'PostHog publishes 131 APIs on the [APIs.io](https://apis.io/) network, including actions API, activity_log API, activity_logs API, and 128 more. Tagged areas include A/B Testing, Analytics, Feature Flags, Open Source, and Product Analytics.


  The PostHog catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  PostHog''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, GitHub presence, signup flow, and 18 more developer resources.'
plans:
- name: Posthog Plans Pricing
  plan_count: 4
  slug: posthog-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 4
  name: Posthog Rate Limits
  slug: posthog-rate-limits
rules:
- name: PostHog API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: posthog-asyncapi-spectral-rules
- name: PostHog API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: posthog-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.1
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 56.4
    developer_ergonomics: 54.3
    discoverability: 66.7
    governance: 41.7
    operational_transparency: 44.7
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 131
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/posthog/refs/heads/main/screenshots/posthog-2026-06-20T192012.png
security:
- kind: authentication
  name: Posthog Authentication
  slug: posthog-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Posthog Domain Security
  slug: posthog-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Posthog Vulnerability Disclosure
  slug: posthog-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Posthog Trust Center
  slug: posthog-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: posthog
tags:
- A/B Testing
- Analytics
- Feature Flags
- Open Source
- Product Analytics
- Session Recording
website: https://posthog.com
---
