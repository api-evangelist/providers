---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Admin API from Edge Impulse — 49 operation(s) for admin.
  name: Edge Impulse Admin API
  phrasing_intents:
  - id: adminGetMetrics
    intent: Get global platform metrics as an admin
    question: As an admin, where do I see the global metrics for the whole Edge Impulse platform?
  - id: adminGetMetricsReports
    intent: List global metrics reports
    question: Which global metrics reports have been generated so far?
  - id: adminCreateMetricsReport
    intent: Generate a global metrics report for a date range
    question: How do I generate a platform metrics report for last quarter?
  - id: adminGetMetricsReport
    intent: Get one global metrics report
    question: Is a specific global metrics report ready, and what period does it cover?
  - id: adminDeleteMetricsReport
    intent: Delete a global metrics report
    question: How do I remove an old global metrics report?
  - id: adminDownloadMetricsReport
    intent: Download a global metrics report
    question: Where do I download the file for a finished global metrics report?
  - id: adminGetDataMigrations
    intent: List data migrations
    question: Which data migrations exist on the platform infrastructure?
  - id: adminGetDataMigration
    intent: Get one data migration
    question: What is the state of a particular data migration?
  phrasing_ops: 72
  slug: edge-impulse-admin-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Auth API from Edge Impulse — 2 operation(s) for auth.
  name: Edge Impulse Auth API
  phrasing_intents:
  - id: discourse
    intent: Sign a user into the Discourse forum
    question: How does single sign-on into the Edge Impulse Discourse forum work?
  - id: readme
    intent: Sign a user into the Readme.io docs
    question: Can I log into the documentation site with my existing account?
  phrasing_ops: 2
  slug: edge-impulse-auth-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Canary API from Edge Impulse — 1 operation(s) for canary.
  name: Edge Impulse Canary API
  phrasing_intents:
  - id: shouldGoOnCanary
    intent: Check whether a URL is routed to the canary deployment
    question: Will a given Edge Impulse URL be served by the canary deployment or the stable one?
  phrasing_ops: 1
  slug: edge-impulse-canary-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The CDN API from Edge Impulse — 1 operation(s) for cdn.
  name: Edge Impulse CDN API
  phrasing_intents:
  - id: getUserCDNResource
    intent: Fetch a file from the user CDN
    question: How do I pull a file off the Edge Impulse user CDN by its path?
  phrasing_ops: 1
  slug: edge-impulse-cdn-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Classify API from Edge Impulse — 10 operation(s) for classify.
  name: Edge Impulse Classify API
  phrasing_intents:
  - id: classifySample
    intent: Classify a sample (deprecated v1)
    question: Is the old GET classify-sample endpoint still usable, or has it been deprecated?
  - id: classifySampleV2
    intent: Classify a sample against the impulse
    question: How do I run my trained impulse over a complete sample file with a sliding window?
  - id: classifySampleForVariants
    intent: Classify a sample across several model variants
    question: Can I compare how float32 and int8 variants classify the same sample in one call?
  - id: getSampleWindowFromCache
    intent: Get cached raw features for a sample window
    question: After live classification finishes, can I fetch the raw features of one window?
  - id: getClassifyJobResult
    intent: Get the full test-set classification result
    question: Where do I see how my model performed across the whole testing dataset?
  - id: getClassifyJobResultPage
    intent: Page through test-set predictions
    question: How do I page through the predictions from a classify-all job?
  - id: getClassifyMetricsAllVariants
    intent: Get test metrics for every model variant
    question: What accuracy did each model variant reach in the last classify-all run?
  - id: classifySampleByLearnBlock
    intent: Classify a sample by learn block (deprecated v1)
    question: Is the v1 anomaly GMM learn-block classify endpoint deprecated?
  phrasing_ops: 10
  slug: edge-impulse-classify-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Deployment API from Edge Impulse — 10 operation(s) for deployment.
  name: Edge Impulse Deployment API
  phrasing_intents:
  - id: listAllDeploymentTargets
    intent: List every deployment target on the platform
    question: Which hardware and library targets can Edge Impulse models be deployed to?
  - id: listDeploymentTargetsForProject
    intent: List deployment targets for a project
    question: Which boards and formats can I deploy my project's impulse to?
  - id: listDeploymentTargetsForProjectDataSources
    intent: List deployment targets for the data sources page
    question: Which Linux deploy targets show up on my project's data sources page?
  - id: getEvaluateJobResult
    intent: Get performance results for impulse variants
    question: How does each variant of my impulse perform before I pick one to deploy?
  - id: getEvaluateJobResultCache
    intent: Check for cached evaluation results
    question: Are evaluation results already cached for my project without running a new job?
  - id: getDeployment
    intent: Check whether a deployment is already built
    question: Has a build already been made for this deployment type in my project?
  - id: downloadBuild
    intent: Download the current deployment build
    question: How do I download the built firmware or library for my project?
  - id: getLastDeploymentBuild
    intent: Get the last successful deployment build
    question: What was my most recent successful deployment and is it still valid?
  phrasing_ops: 16
  slug: edge-impulse-deployment-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Devices API from Edge Impulse — 11 operation(s) for devices.
  name: Edge Impulse Devices API
  phrasing_intents:
  - id: listDevices
    intent: List a project's devices
    question: Which devices are connected to my Edge Impulse project?
  - id: getDevice
    intent: Get one device's details
    question: Can I look up a single device and see its sensors and status?
  - id: deleteDevice
    intent: Delete a device
    question: Can I remove a device from my project?
  - id: startSampling
    intent: Start sampling data on a device
    question: How do I trigger a device to record a labeled sample remotely?
  - id: startDeviceInferenceDebugStream
    intent: Start an inference debug stream
    question: Can I watch live inference results from a device as they happen?
  - id: startDeviceSnapshotDebugStream
    intent: Start a camera snapshot debug stream
    question: Can I see a live camera view from a device?
  - id: keepDeviceDebugStreamAlive
    intent: Keep a device debug stream alive
    question: What happens if I stop pinging an open device debug stream?
  - id: stopDeviceDebugStream
    intent: Stop a device debug stream
    question: Can I close a debug stream I opened on a device?
  phrasing_ops: 12
  slug: edge-impulse-devices-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The DSP API from Edge Impulse — 18 operation(s) for dsp.
  name: Edge Impulse DSP API
  phrasing_intents:
  - id: getDspConfig
    intent: Get a DSP block's configuration
    question: How do I read the current parameters of a DSP processing block in my impulse?
  - id: setDspConfig
    intent: Update a DSP block's configuration
    question: Can I change only some DSP block parameters without overwriting the rest?
  - id: clearDspBlock
    intent: Clear a DSP block's generated features
    question: How do I wipe the features a DSP block has already generated?
  - id: getDspMetadata
    intent: Get metadata from a generated DSP block
    question: What metadata does a DSP block record after features are generated?
  - id: getDspRawSample
    intent: Get a raw sample filtered to the DSP block's axes
    question: How do I view a full raw sample showing only the axes my DSP block uses?
  - id: getDspSampleSlice
    intent: Get a slice of raw sample data for a DSP block
    question: Can I fetch just a time window of raw data from a sample, before processing?
  - id: runDspSampleSlice
    intent: Process a sample slice with custom parameters
    question: How do I preview what a DSP block outputs for a window using parameters I haven't saved?
  - id: runDspSampleSliceReadOnly
    intent: Process a sample slice with saved parameters
    question: Is there a read-only way to see processed output for a slice using the block's saved settings?
  phrasing_ops: 19
  slug: edge-impulse-dsp-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Export API from Edge Impulse — 1 operation(s) for export.
  name: Edge Impulse Export API
  phrasing_intents:
  - id: getExportUrl
    intent: Get the link to a project's exported artefacts
    question: Where can I find the URL for the files produced by my last export job?
  - id: downloadExport
    intent: Download a project's data export
    question: How do I download the data export I generated for my Edge Impulse project?
  phrasing_ops: 2
  slug: edge-impulse-export-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Health API from Edge Impulse — 2 operation(s) for health.
  name: Edge Impulse Health API
  phrasing_intents:
  - id: health
    intent: Check studio web container health
    question: Are the Studio web front-end containers healthy?
  - id: apiHealth
    intent: Check studio API container health
    question: Is the Studio API backend up right now?
  phrasing_ops: 2
  slug: edge-impulse-health-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Impulse API from Edge Impulse — 13 operation(s) for impulse.
  name: Edge Impulse API
  phrasing_intents:
  - id: getImpulse
    intent: Get a project's impulse design
    question: What input, processing and learning blocks make up my project's default impulse?
  - id: createImpulse
    intent: Set an impulse's input, DSP and learn blocks
    question: How do I define the full pipeline of input, signal processing and learning blocks for an Edge Impulse project?
  - id: deleteImpulse
    intent: Clear an impulse and all its blocks
    question: How do I wipe the impulse design of a project and start over?
  - id: createNewEmptyImpulse
    intent: Create a new empty impulse
    question: Can I add another blank impulse to a project to try a different experiment?
  - id: updateImpulse
    intent: Rename or tag an impulse
    question: How do I rename one of my impulse experiments?
  - id: getImpulseAll
    intent: Get an impulse including disabled blocks
    question: Can I see the blocks I disabled in my impulse, not just the active ones?
  - id: getNewBlockId
    intent: Get an unused block ID for an impulse
    question: How do I avoid reusing a block ID when building an impulse by hand?
  - id: getImpulseBlocks
    intent: List blocks available for building an impulse
    question: Which processing and learning blocks can I choose from when designing an impulse?
  phrasing_ops: 18
  slug: edge-impulse-impulse-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Jobs API from Edge Impulse — 42 operation(s) for jobs.
  name: Edge Impulse Jobs API
  phrasing_intents:
  - id: startPostProcessingJob
    intent: Start a post-processing tuning job
    question: How do I tune the post-processing of my model's output with a search algorithm?
  - id: generateDataExplorerFeatures
    intent: Generate features for the data explorer
    question: How do I populate the data explorer so I can see my samples clustered visually?
  - id: calculateDataQualityMetrics
    intent: Calculate data quality metrics for a dataset
    question: Is there a staff-only job that scores the quality of a project's dataset?
  - id: retryImpulseMigration
    intent: Retry a failed impulse migration
    question: My multi-impulse migration failed — how do I try it again?
  - id: createSyntheticDataJob
    intent: Generate synthetic training data
    question: How do I generate synthetic samples to grow a small dataset?
  - id: createPreviewAIActionsJob
    intent: Dry-run an AI Action on sample data
    question: Can I preview what an AI Action would change on a few samples before applying it?
  - id: createAIActionsJob
    intent: Run an AI Action and apply its changes
    question: How do I run an AI Action so it actually updates my dataset?
  - id: optimizeJob
    intent: Run the EON Tuner to find the best model
    question: How do I let the EON Tuner search for the optimal model architecture for my data?
  phrasing_ops: 44
  slug: edge-impulse-jobs-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Learn API from Edge Impulse — 21 operation(s) for learn.
  name: Edge Impulse Learn API
  phrasing_intents:
  - id: getLearnXData
    intent: Download processed features for a learning block
    question: How do I download the processed feature data a learning block trains on?
  - id: getLearnYData
    intent: Download labels for a learning block
    question: Where can I download the training labels for a learning block?
  - id: getAnomaly
    intent: Get an anomaly block's configuration
    question: What does my anomaly detection block depend on and how is it configured?
  - id: setAnomaly
    intent: Set an anomaly block's minimum confidence
    question: How do I change the anomaly threshold on my anomaly detection block?
  - id: getAnomalyMetadata
    intent: Get metadata for a trained anomaly block
    question: What metadata is available after my anomaly block has been trained?
  - id: getGmmMetadata
    intent: Get the GMM model metadata of an anomaly block
    question: Can I get the raw Gaussian mixture model parameters from my anomaly block?
  - id: getKeras
    intent: Get a Keras block's configuration
    question: How is my Keras neural network block currently configured?
  - id: setKeras
    intent: Configure Keras training settings
    question: How do I change the number of training cycles and learning rate for my neural network?
  phrasing_ops: 26
  slug: edge-impulse-learn-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Login API from Edge Impulse — 1 operation(s) for login.
  name: Edge Impulse Login API
  phrasing_intents:
  - id: login
    intent: Sign in and get an API token
    question: How do I get a JWT token to call the Edge Impulse API?
  - id: getSSODomainIdPs
    intent: Look up single sign-on providers for a user
    question: Which identity providers can a given user or email domain sign in with?
  phrasing_ops: 2
  slug: edge-impulse-login-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Metrics API from Edge Impulse — 3 operation(s) for metrics.
  name: Edge Impulse Metrics API
  phrasing_intents:
  - id: getPublicMetrics
    intent: Get public platform usage numbers
    question: How many projects and data samples are on Edge Impulse right now?
  - id: logWebsitePageview
    intent: Record a website pageview
    question: How do I record a page view for website analytics?
  - id: logAnalyticsEvent
    intent: Record a named analytics event
    question: How do I send a custom analytics event with properties?
  phrasing_ops: 3
  slug: edge-impulse-metrics-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Optimization API from Edge Impulse — 15 operation(s) for optimization.
  name: Edge Impulse Optimization API
  phrasing_intents:
  - id: listTunerRuns
    intent: List EON Tuner runs for a project
    question: What EON Tuner runs have been executed on my Edge Impulse project?
  - id: getConfig
    intent: Get the EON Tuner configuration
    question: What target device and latency is the EON Tuner currently configured for?
  - id: updateConfig
    intent: Configure the EON Tuner
    question: How do I set a target device and latency budget for the EON Tuner?
  - id: getAllLearnBlocks
    intent: List learn blocks available to the tuner
    question: Which learning blocks can the EON Tuner choose from in my project?
  - id: getWindowSettings
    intent: Get the tuner's window settings
    question: What window size and stride settings will the EON Tuner explore?
  - id: scoreTrial
    intent: Score a candidate tuner trial
    question: Can I estimate how a combination of input, DSP and learn blocks would score before running it?
  - id: createTrial
    intent: Create a trial within a tuner job
    question: How do I add a new trial to an EON Tuner job that's already running?
  - id: completeSearch
    intent: Mark an EON Tuner run as complete
    question: How do I finish an EON Tuner run and record whether it succeeded?
  phrasing_ops: 18
  slug: edge-impulse-optimization-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The OrganizationBlocks API from Edge Impulse — 17 operation(s) for organizationblocks.
  name: Edge Impulse OrganizationBlocks API
  phrasing_intents:
  - id: listOrganizationTransformationBlocks
    intent: List an organization's transformation blocks
    question: What transformation blocks has my Edge Impulse organization created?
  - id: addOrganizationTransformationBlock
    intent: Add a transformation block
    question: How do I register a Docker container as a data transformation block?
  - id: listPublicOrganizationTransformationBlocks
    intent: List public transformation blocks
    question: Which transformation blocks have other organizations published for everyone to use?
  - id: getPublicOrganizationTransformationBlock
    intent: Get a public transformation block
    question: What does a specific public transformation block from another organization do?
  - id: getOrganizationTransformationBlock
    intent: Get one of our transformation blocks
    question: What container and CLI arguments does one of our transformation blocks use?
  - id: updateOrganizationTransformationBlock
    intent: Update a transformation block
    question: How do I change the Docker image of an existing transformation block?
  - id: deleteOrganizationTransformationBlock
    intent: Delete a transformation block
    question: How do I remove a transformation block my organization no longer uses?
  - id: exportOrganizationTransformationBlock
    intent: Download a transformation block's source
    question: Can I download the source code behind a transformation block?
  phrasing_ops: 30
  slug: edge-impulse-organizationblocks-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The OrganizationCreateProject API from Edge Impulse — 10 operation(s) for organizationcreateproject.
  name: Edge Impulse OrganizationCreateProject API
  phrasing_intents:
  - id: getOrganizationCreateProjects
    intent: List an organization's transformation jobs
    question: Which transformation jobs has my organization run against its datasets?
  - id: organizationCreateProject
    intent: Start a transformation job
    question: How do I pull files from my organization's dataset into a new or existing project?
  - id: getOrganizationCreateProjectStatus
    intent: Check a transformation job's status
    question: How far along is my transformation job, and which files have failed?
  - id: updateOrganizationCreateProject
    intent: Update a running transformation job
    question: Can I change how many files a transformation job processes in parallel after it started?
  - id: deleteOrganizationCreateProject
    intent: Delete a transformation job
    question: Does removing a transformation job stop the jobs it's still running?
  - id: retryOrganizationTransform
    intent: Retry failed transform jobs
    question: Can I rerun only the transform steps that failed in a transformation job?
  - id: clearOrganizationTransform
    intent: Clear failed transform jobs
    question: How do I discard failed transform entries instead of retrying them?
  - id: retryOrganizationUpload
    intent: Retry a transformation job's upload step
    question: The upload into my project failed after transforming; can I retry just that step?
  phrasing_ops: 15
  slug: edge-impulse-organizationcreateproject-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The OrganizationData API from Edge Impulse — 32 operation(s) for organizationdata.
  name: Edge Impulse OrganizationData API
  phrasing_intents:
  - id: listOrganizationBuckets
    intent: List an organization's storage buckets
    question: Which storage buckets are connected to my Edge Impulse organization?
  - id: addOrganizationBucket
    intent: Connect an external storage bucket
    question: How do I connect my own S3 or GCS bucket to an organization?
  - id: verifyOrganizationBucket
    intent: Test bucket credentials before connecting
    question: Can I check that new bucket credentials work before I add the bucket?
  - id: getOrganizationBucket
    intent: Get a storage bucket's details
    question: What endpoint and region is a connected bucket configured with?
  - id: updateOrganizationBucket
    intent: Update a storage bucket's settings
    question: How do I rotate the access keys on a connected bucket?
  - id: removeOrganizationBucket
    intent: Remove a storage bucket
    question: What happens to data when I disconnect a storage bucket from my organization?
  - id: verifyExistingOrganizationBucket
    intent: Check access to an already-connected bucket
    question: Is my already-connected bucket still reachable under a given prefix?
  - id: listOrganizationData
    intent: List an organization's data items
    question: What data items are in my organization's datasets?
  phrasing_ops: 40
  slug: edge-impulse-organizationdata-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The OrganizationDataCampaigns API from Edge Impulse — 7 operation(s) for organizationdatacampaigns.
  name: Edge Impulse OrganizationDataCampaigns API
  phrasing_intents:
  - id: getOrganizationDataCampaignDashboards
    intent: List an organization's data campaign dashboards
    question: What data campaign dashboards does my organization have?
  - id: addOrganizationDataCampaignDashboard
    intent: Create a data campaign dashboard
    question: How do I set up a dashboard that emails progress on our data collection campaigns?
  - id: getOrganizationDataCampaignDashboard
    intent: Get a data campaign dashboard
    question: How is a particular campaign dashboard configured, and who receives its emails?
  - id: updateOrganizationDataCampaignDashboard
    intent: Update a data campaign dashboard
    question: How do I change who gets the email from an existing campaign dashboard?
  - id: deleteOrganizationDataCampaignDashboard
    intent: Delete a data campaign dashboard
    question: How do I get rid of a campaign dashboard we no longer use?
  - id: getOrganizationDataCampaignsForDashboard
    intent: List the campaigns on a dashboard
    question: Which data campaigns are shown on a given dashboard?
  - id: uploadDashboardScreenshot
    intent: Upload a screenshot of a campaign dashboard
    question: Is there an internal way to store a screenshot image of a campaign dashboard?
  - id: addOrganizationDataCampaign
    intent: Add a data campaign to a dashboard
    question: How do I start tracking a new data collection campaign on a dashboard?
  phrasing_ops: 12
  slug: edge-impulse-organizationdatacampaigns-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The OrganizationPipelines API from Edge Impulse — 5 operation(s) for organizationpipelines.
  name: Edge Impulse OrganizationPipelines API
  phrasing_intents:
  - id: listOrganizationPipelines
    intent: List an organization's pipelines
    question: What data pipelines does my Edge Impulse organization have set up?
  - id: createOrganizationPipeline
    intent: Create an organizational pipeline
    question: How do I set up a new pipeline of steps that runs on a schedule for my organization?
  - id: listArchivedOrganizationPipelines
    intent: List archived organizational pipelines
    question: Where can I find pipelines that were archived in my organization?
  - id: getOrganizationPipeline
    intent: Get one organizational pipeline
    question: What steps and schedule are configured on a specific pipeline?
  - id: updateOrganizationPipeline
    intent: Update an existing organizational pipeline
    question: How do I change the steps or schedule of a pipeline I already created?
  - id: deleteOrganizationPipeline
    intent: Delete an organizational pipeline
    question: How do I permanently remove a pipeline from my organization?
  - id: runOrganizationPipeline
    intent: Run an organizational pipeline now
    question: Can I trigger a pipeline immediately instead of waiting for its schedule?
  - id: stopOrganizationPipeline
    intent: Stop a running pipeline
    question: How do I halt a pipeline that is currently running?
  phrasing_ops: 8
  slug: edge-impulse-organizationpipelines-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The OrganizationPortals API from Edge Impulse — 7 operation(s) for organizationportals.
  name: Edge Impulse OrganizationPortals API
  phrasing_intents:
  - id: listOrganizationPortals
    intent: List an organization's upload portals
    question: Which upload portals are configured for my Edge Impulse organization?
  - id: getOrganizationPortal
    intent: Get details of an upload portal
    question: Which bucket and path does a particular upload portal write to?
  - id: verifyOrganizationPortal
    intent: Preview files in an upload portal
    question: Can I preview a sample of files in an upload portal before adding it as a data source?
  - id: createOrganizationPortal
    intent: Create an upload portal
    question: How do I create an upload portal that drops files into one of my storage buckets?
  - id: updateOrganizationPortal
    intent: Update an existing upload portal
    question: How do I point an existing upload portal at a different bucket path?
  - id: rotateOrganizationPortalToken
    intent: Rotate an upload portal's token
    question: How do I invalidate an upload portal's access token and get a new one?
  - id: deleteOrganizationPortal
    intent: Delete an upload portal
    question: How do I remove an upload portal I no longer need?
  phrasing_ops: 7
  slug: edge-impulse-organizationportals-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Organizations API from Edge Impulse — 60 operation(s) for organizations.
  name: Edge Impulse Organizations API
  phrasing_intents:
  - id: listOrganizations
    intent: List organizations I belong to
    question: Which Edge Impulse organizations am I a member of?
  - id: createOrganization
    intent: Create a new organization
    question: How do I set up a brand-new organization for my team?
  - id: getOrganizationInfo
    intent: Get an organization's details
    question: Where do I see all the information about my organization?
  - id: updateOrganization
    intent: Update my organization's settings
    question: How do I rename my organization or change its readme?
  - id: deleteOrganization
    intent: Permanently delete my organization
    question: Is deleting my organization and all its data reversible?
  - id: requestEnterpriseTrialExtension
    intent: Request an enterprise trial extension
    question: My enterprise trial is ending; can I ask for more time?
  - id: getOrganizationMetrics
    intent: Get usage metrics for my organization
    question: What general usage metrics are available for my organization?
  - id: requestEnterpriseHrBlockLicense
    intent: Request a license for the HR block
    question: What license do I need to deploy an impulse that uses the HR block?
  phrasing_ops: 80
  slug: edge-impulse-organizations-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The PerformanceCalibration API from Edge Impulse — 9 operation(s) for performancecalibration.
  name: Edge Impulse PerformanceCalibration API
  phrasing_intents:
  - id: getPerformanceCalibrationStatus
    intent: Get performance calibration status
    question: Is performance calibration still running on my project?
  - id: getPerformanceCalibrationGroundTruth
    intent: Get calibration ground truth data
    question: What ground truth labels did performance calibration use?
  - id: getPerformanceCalibrationRawResult
    intent: Get raw calibration results
    question: Can I see the unprocessed output of a performance calibration run?
  - id: getPerformanceCalibrationParameterSets
    intent: List calibration parameter sets
    question: Which post-processing parameter sets did calibration suggest?
  - id: getPerformanceCalibrationSavedParameters
    intent: Get saved calibration parameters
    question: Which performance calibration parameters are currently saved for my project?
  - id: setPerformanceCalibrationSavedParameters
    intent: Save performance calibration parameters
    question: How do I keep a chosen set of performance calibration parameters?
  - id: deletePerformanceCalibrationSavedParameters
    intent: Clear saved calibration parameters
    question: Can I remove the calibration parameters I saved?
  - id: getWavFile
    intent: Download the synthetic calibration WAV
    question: Can I listen to the synthetic audio sample used for calibration?
  phrasing_ops: 11
  slug: edge-impulse-performancecalibration-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Projects API from Edge Impulse — 46 operation(s) for projects.
  name: Edge Impulse Projects API
  phrasing_intents:
  - id: listProjects
    intent: List the projects I can access
    question: Which Edge Impulse projects does my account have access to?
  - id: createProject
    intent: Create a new project
    question: How do I start a brand-new Edge Impulse project?
  - id: listDevkeys
    intent: Get a project's development API and HMAC keys
    question: Where do I find the development API key and HMAC key together for a project?
  - id: listDownloads
    intent: List a project's downloadable files
    question: What files can I download from my project, like trained models or datasets?
  - id: downloadCsvWizardConfig
    intent: Download the CSV Wizard config
    question: Can I export the CSV Wizard configuration of a project as a JSON file?
  - id: getCsvWizardUploadedFileInfo
    intent: Check if the CSV Wizard source file exists
    question: Is the sample file I used to set up the CSV Wizard still available?
  - id: uploadCsvWizardUploadedFile
    intent: Store the CSV Wizard source file
    question: Can I save the CSV file the wizard was based on alongside the project?
  - id: downloadCsvWizardUploadedFile
    intent: Download the CSV Wizard source file
    question: How can I get back the original CSV I used to configure the CSV Wizard?
  phrasing_ops: 60
  slug: edge-impulse-projects-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Raw data API from Edge Impulse — 54 operation(s) for raw data.
  name: Edge Impulse Raw data API
  phrasing_intents:
  - id: listSamples
    intent: List data samples in a dataset category
    question: What samples are in the training set of my Edge Impulse project?
  - id: countSamples
    intent: Count data samples in a dataset category
    question: How many training samples does my project have?
  - id: getObjectDetectionLabelQueue
    intent: Get images waiting for bounding-box labeling
    question: Which images still need bounding boxes drawn in my object detection project?
  - id: getObjectDetectionLabelQueueCount
    intent: Count items in the object detection labeling queue
    question: How many images are left to label in my object detection queue?
  - id: rebalanceDataset
    intent: Rebalance train/test split (original endpoint)
    question: How do I reset my dataset to an 80/20 train-test split using the original rebalance endpoint?
  - id: clearAllObjectDetectionLabels
    intent: Clear all bounding-box labels in a project
    question: How do I wipe every bounding box in my dataset and start labeling over?
  - id: deleteAllSamples
    intent: Delete all samples in a project
    question: How do I delete my entire dataset across training and testing?
  - id: deleteAllSamplesByCategory
    intent: Delete all samples in one category
    question: Can I delete just the test set while keeping training data?
  phrasing_ops: 66
  slug: edge-impulse-raw-data-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Themes API from Edge Impulse — 5 operation(s) for themes.
  name: Edge Impulse Themes API
  phrasing_intents:
  - id: getThemes
    intent: List available Studio themes
    question: What Studio themes are available in Edge Impulse?
  - id: getTheme
    intent: Get a Studio theme
    question: How do I look up the logos and colors of one specific Studio theme?
  - id: deleteTheme
    intent: Delete a Studio theme
    question: Can I remove a Studio theme I no longer need?
  - id: updateThemeLogos
    intent: Update a theme's logos
    question: How do I swap the primary, login and mark logos on a Studio theme?
  - id: updateThemeColors
    intent: Update a theme's colors
    question: How do I change the primary color of a Studio theme?
  - id: updateThemeFavicon
    intent: Update a theme's favicon
    question: How do I upload a new browser favicon for a Studio theme?
  phrasing_ops: 6
  slug: edge-impulse-themes-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The UploadPortal API from Edge Impulse — 7 operation(s) for uploadportal.
  name: Edge Impulse UploadPortal API
  phrasing_intents:
  - id: getPortalInfo
    intent: Get details about an upload portal
    question: What information can I see about an Edge Impulse upload portal?
  - id: createSignedUploadLink
    intent: Create a signed link to upload a file to a portal
    question: How can a client upload a file straight to the portal's storage bucket without going through the server?
  - id: listPortalFilesInFolder
    intent: List files and folders in an upload portal
    question: What files have been uploaded to a portal folder so far?
  - id: deletePortalFile
    intent: Delete a file from an upload portal
    question: How do I remove a file someone uploaded to my portal by mistake?
  - id: renamePortalFile
    intent: Rename or move a file in an upload portal
    question: Can I rename a file after it was uploaded to a portal?
  - id: downloadPortalFile
    intent: Get a download link for a portal file
    question: How do I download the original file someone put in my upload portal?
  - id: viewPortalFile
    intent: Preview a file stored in an upload portal
    question: Can I preview a Parquet or CSV file in a portal without downloading it?
  phrasing_ops: 7
  slug: edge-impulse-uploadportal-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The User API from Edge Impulse — 43 operation(s) for user.
  name: Edge Impulse User API
  phrasing_intents:
  - id: createUser
    intent: Sign up a new user with a first project
    question: How do I register a new Edge Impulse account and get a starter project?
  - id: createEvaluationUser
    intent: Create a throwaway evaluation account
    question: Can I try the platform with an evaluation account without filling in my details?
  - id: createProTierUser
    intent: Sign up a user on the Professional plan
    question: How do I sign up directly for the Professional plan?
  - id: createEnterpriseTrialUser
    intent: Sign up a new user with an enterprise trial
    question: Can a brand-new user sign up and get an enterprise trial organization at the same time?
  - id: getUserNeedToSetPassword
    intent: Check whether a user is registered and needs a password
    question: Is there already an account for this email, and does it still need a password set?
  - id: getCurrentUser
    intent: Get my own user profile
    question: What account details does Edge Impulse have for me?
  - id: updateCurrentUser
    intent: Update my own profile details
    question: How do I change my display name or job title on my own account?
  - id: deleteCurrentUser
    intent: Delete my own account
    question: How do I permanently close my own account?
  phrasing_ops: 49
  slug: edge-impulse-user-api
- description: The Ingestion API sends new device data into an Edge Impulse project. It accepts sensor (JSON/CBOR/CSV/Parquet), audio (WAV), image (JPG/PNG) and video (MP4/AVI) samples on the training, validation, t
  name: Edge Impulse Ingestion API
  slug: edge-impulse-ingestion-api
- baseURL: https://remote-mgmt.edgeimpulse.com
  baseurl_source: declared
  description: 'A two-way WebSocket protocol between edge devices and Edge Impulse Studio, used to drive a connected device — request a sample, follow acquisition progress and stream snapshot frames. Devices connect '
  name: Edge Impulse Remote Management API
  slug: edge-impulse-remote-management-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Integrations API from Edge Impulse — 2 operation(s) for integrations.
  name: Edge Impulse Integrations API
  phrasing_intents:
  - id: startTensorBoardSession
    intent: Start a TensorBoard session for learn blocks
    question: How do I open TensorBoard to inspect training of my Edge Impulse learning blocks?
  - id: getTensorBoardSessionStatus
    intent: Check the status of a TensorBoard session
    question: Is my TensorBoard session ready yet?
  phrasing_ops: 2
  slug: edge-impulse-integrations-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The PostProcessing API from Edge Impulse — 3 operation(s) for postprocessing.
  name: Edge Impulse Post Processing API
  phrasing_intents:
  - id: getPostProcessingConfig
    intent: Get a post-processing block's config
    question: How do I read the current settings of a post-processing block in my impulse?
  - id: setPostProcessingConfig
    intent: Configure a post-processing block
    question: Can I turn a post-processing block on or off and change its parameters?
  - id: getPostProcessingResultsForSample
    intent: Check post-processing results for a sample
    question: Has post-processing already generated features for this sample?
  - id: generatePostProcessingFeaturesForSample
    intent: Classify a sample with post-processing
    question: How do I run a classification on a sample with post-processing applied?
  phrasing_ops: 4
  slug: edge-impulse-postprocessing-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Email Verification API from Edge Impulse — 4 operation(s) for email verification.
  name: Edge Impulse Email Verification API
  phrasing_intents:
  - id: requestEmailVerification
    intent: Send an email verification code
    question: How do I get Edge Impulse to send an activation code to an email address?
  - id: verifyEmail
    intent: Verify an email address with a code
    question: What do I do with the verification code I received by email?
  - id: validateEmail
    intent: Check if an email is valid for sign-up
    question: Is this email address acceptable for creating a new account?
  - id: getEmailVerificationStatus
    intent: Get the status of an email verification
    question: Has a pending email verification request been completed yet?
  phrasing_ops: 4
  slug: edge-impulse-email-verification-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Feature Flags API from Edge Impulse — 1 operation(s) for feature flags.
  name: Edge Impulse Feature Flags API
  phrasing_intents:
  - id: getFeatureFlags
    intent: List global feature flags and their status
    question: Which global feature flags are currently enabled in Edge Impulse?
  phrasing_ops: 1
  slug: edge-impulse-feature-flags-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Organization Jobs API from Edge Impulse — 8 operation(s) for organization jobs.
  name: Edge Impulse Organization Jobs API
  phrasing_intents:
  - id: listActiveOrganizationJobs
    intent: List an organization's running jobs
    question: Which jobs are currently running in my organization?
  - id: listFinishedOrganizationJobs
    intent: List an organization's finished jobs
    question: What jobs has my organization completed over the last week?
  - id: listAllOrganizationJobs
    intent: List all jobs in an organization
    question: How can I see both running and finished jobs for my organization in one list?
  - id: cancelOrganizationJob
    intent: Cancel a running organization job
    question: How do I stop a job that is running in my organization?
  - id: getOrganizationJobStatus
    intent: Check the status of an organization job
    question: Is my organization job finished yet or still running?
  - id: getOrganizationJobsLogs
    intent: View an organization job's logs
    question: Where can I read the output of an organization job to see why it failed?
  - id: downloadOrganizationJobsLogs
    intent: Download an organization job's logs as text
    question: Can I save an organization job's log output as a text file?
  - id: getOrganizationSocketToken
    intent: Get a websocket token for an organization
    question: How do I authenticate to the websocket to stream organization job updates?
  phrasing_ops: 8
  slug: edge-impulse-organization-jobs-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The Third Party Auth API from Edge Impulse — 4 operation(s) for third party auth.
  name: Edge Impulse Third Party Auth API
  phrasing_intents:
  - id: getAllThirdPartyAuth
    intent: List third-party auth partners
    question: Which third-party authentication partners are registered?
  - id: createThirdPartyAuth
    intent: Register a third-party auth partner
    question: How do I register a new third-party authentication partner?
  - id: getThirdPartyAuth
    intent: Get a third-party auth partner
    question: What domains and logo are set on a particular auth partner?
  - id: updateThirdPartyAuth
    intent: Update a third-party auth partner
    question: Can I change the allowed domains of an auth partner?
  - id: deleteThirdPartyAuth
    intent: Delete a third-party auth partner
    question: Can I remove a third-party authentication partner?
  - id: authorizeThirdParty
    intent: Grant a third party access to a project
    question: How do I let a third-party partner access one of my projects?
  - id: createUserThirdParty
    intent: Log in or create a user as a partner
    question: As an auth partner, can I sign users in and auto-create their accounts?
  phrasing_ops: 7
  slug: edge-impulse-third-party-auth-api
- baseURL: https://studio.edgeimpulse.com/v1
  baseurl_source: declared
  description: The White Labels API from Edge Impulse — 5 operation(s) for white labels.
  name: Edge Impulse White Labels API
  phrasing_intents:
  - id: getAllWhitelabels
    intent: List registered white labels
    question: Which white-label instances are registered on Edge Impulse?
  - id: createWhitelabel
    intent: Create a new white label
    question: How do I set up a new white-label instance on its own domain?
  - id: getWhitelabel
    intent: Get a white label's full details
    question: What settings does a specific white label have?
  - id: updateWhitelabel
    intent: Change a white label's organization limit
    question: How do I raise the number of organizations a white label can have?
  - id: deleteWhitelabel
    intent: Delete a white label
    question: How do I remove a white label I no longer need?
  - id: getWhitelabelDomain
    intent: Get the domain of a white label
    question: What domain is a particular white label served on?
  - id: updateDeploymentTargets
    intent: Choose deployment targets for a white label
    question: How do I limit which deployment targets users of a white label can build for?
  - id: getAllImpulseBlocks
    intent: List DSP and ML blocks for a white label
    question: Which processing and learning blocks are available on a white label?
  phrasing_ops: 8
  slug: edge-impulse-white-labels-api
artifact_total: 91
asyncapis:
- description: DERIVED, NOT PUBLISHED. Edge Impulse does not ship an AsyncAPI document. This one is derived by API Evangelist from the provider's own written WebSocket protocol reference at https://docs.edgeimpulse.
  name: Edge Impulse Remote Management API
  slug: edge-impulse-remote-management-asyncapi
- description: ''
  name: Edge Impulse Webhooks
  slug: edge-impulse-webhooks
collections:
- collection_type: open
  name: Edge Impulse Admin API
  slug: open-edge-impulse-admin-api
- collection_type: open
  name: Edge Impulse Auth API
  slug: open-edge-impulse-auth-api
- collection_type: open
  name: Edge Impulse Canary API
  slug: open-edge-impulse-canary-api
- collection_type: open
  name: Edge Impulse CDN API
  slug: open-edge-impulse-cdn-api
- collection_type: open
  name: Edge Impulse Classify API
  slug: open-edge-impulse-classify-api
- collection_type: open
  name: Edge Impulse Deployment API
  slug: open-edge-impulse-deployment-api
- collection_type: open
  name: Edge Impulse Devices API
  slug: open-edge-impulse-devices-api
- collection_type: open
  name: Edge Impulse DSP API
  slug: open-edge-impulse-dsp-api
- collection_type: open
  name: Edge Impulse EmailVerification API
  slug: open-edge-impulse-emailverification-api
- collection_type: open
  name: Edge Impulse Export API
  slug: open-edge-impulse-export-api
- collection_type: open
  name: Edge Impulse FeatureFlags API
  slug: open-edge-impulse-featureflags-api
- collection_type: open
  name: Edge Impulse Health API
  slug: open-edge-impulse-health-api
- collection_type: open
  name: Edge Impulse API
  slug: open-edge-impulse-impulse-api
- collection_type: open
  name: Edge Impulse Jobs API
  slug: open-edge-impulse-jobs-api
- collection_type: open
  name: Edge Impulse Learn API
  slug: open-edge-impulse-learn-api
- collection_type: open
  name: Edge Impulse Login API
  slug: open-edge-impulse-login-api
- collection_type: open
  name: Edge Impulse Metrics API
  slug: open-edge-impulse-metrics-api
- collection_type: open
  name: Edge Impulse Optimization API
  slug: open-edge-impulse-optimization-api
- collection_type: open
  name: Edge Impulse OrganizationBlocks API
  slug: open-edge-impulse-organizationblocks-api
- collection_type: open
  name: Edge Impulse OrganizationCreateProject API
  slug: open-edge-impulse-organizationcreateproject-api
- collection_type: open
  name: Edge Impulse OrganizationData API
  slug: open-edge-impulse-organizationdata-api
- collection_type: open
  name: Edge Impulse OrganizationDataCampaigns API
  slug: open-edge-impulse-organizationdatacampaigns-api
- collection_type: open
  name: Edge Impulse OrganizationJobs API
  slug: open-edge-impulse-organizationjobs-api
- collection_type: open
  name: Edge Impulse OrganizationPipelines API
  slug: open-edge-impulse-organizationpipelines-api
- collection_type: open
  name: Edge Impulse OrganizationPortals API
  slug: open-edge-impulse-organizationportals-api
- collection_type: open
  name: Edge Impulse Organizations API
  slug: open-edge-impulse-organizations-api
- collection_type: open
  name: Edge Impulse PerformanceCalibration API
  slug: open-edge-impulse-performancecalibration-api
- collection_type: open
  name: Edge Impulse Projects API
  slug: open-edge-impulse-projects-api
- collection_type: open
  name: Edge Impulse Raw data API
  slug: open-edge-impulse-raw-data-api
- collection_type: open
  name: Edge Impulse Themes API
  slug: open-edge-impulse-themes-api
- collection_type: open
  name: Edge Impulse ThirdPartyAuth API
  slug: open-edge-impulse-thirdpartyauth-api
- collection_type: open
  name: Edge Impulse UploadPortal API
  slug: open-edge-impulse-uploadportal-api
- collection_type: open
  name: Edge Impulse User API
  slug: open-edge-impulse-user-api
- collection_type: open
  name: Edge Impulse Whitelabels API
  slug: open-edge-impulse-whitelabels-api
common:
- group: commercial
  href: https://artifacts.apis.io/edge-impulse/plans/edge-impulse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/edge-impulse-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/edge-impulse/rate-limits/edge-impulse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/edge-impulse-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/edge-impulse/finops/edge-impulse-finops.yml
  title: ''
  type: FinOps
  url: finops/edge-impulse-finops.yml
- group: other
  href: https://artifacts.apis.io/edge-impulse/overlays/edge-impulse-emailverification-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/edge-impulse-emailverification-overlay.yaml
- group: other
  href: https://artifacts.apis.io/edge-impulse/overlays/edge-impulse-featureflags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/edge-impulse-featureflags-overlay.yaml
- group: other
  href: https://artifacts.apis.io/edge-impulse/overlays/edge-impulse-organizationjobs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/edge-impulse-organizationjobs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/edge-impulse/overlays/edge-impulse-thirdpartyauth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/edge-impulse-thirdpartyauth-overlay.yaml
- group: other
  href: https://artifacts.apis.io/edge-impulse/overlays/edge-impulse-whitelabels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/edge-impulse-whitelabels-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/edge-impulse/authentication/edge-impulse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/edge-impulse-authentication.yml
- group: other
  href: https://artifacts.apis.io/edge-impulse/capabilities/edge-impulse-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/edge-impulse-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/edge-impulse/security/edge-impulse-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/edge-impulse-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/edge-impulse/security/edge-impulse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edge-impulse-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edgeimpulse
- group: company
  title: ''
  type: Website
  url: https://edgeimpulse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edgeimpulse.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.edgeimpulse.com/blog/
- group: operate
  title: ''
  type: FAQ
  url: https://edgeimpulse.com/faqs
- group: company
  title: ''
  type: About
  url: https://edgeimpulse.com/about
- group: other
  title: ''
  type: Events
  url: https://edgeimpulse.com/events
- group: operate
  title: ''
  type: Forums
  url: https://forum.edgeimpulse.com/
- group: other
  title: ''
  type: CaseStudies
  url: https://edgeimpulse.com/case-studies
- group: commercial
  title: ''
  type: Plans
  url: https://edgeimpulse.com/pricing
- group: start
  title: ''
  type: Login
  url: https://studio.edgeimpulse.com/login
- group: start
  title: ''
  type: Signup
  url: https://studio.edgeimpulse.com/signup
- group: auth
  title: ''
  type: Security
  url: https://edgeimpulse.com/security
- group: other
  title: ''
  type: Branding
  url: https://edgeimpulse.com/branding
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edgeimpulse
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.edgeimpulse.com/llms.txt
- group: build
  href: https://artifacts.apis.io/edge-impulse/packages/edge-impulse-packages.yml
  title: ''
  type: Packages
  url: packages/edge-impulse-packages.yml
- group: build
  href: https://artifacts.apis.io/edge-impulse/packages/edge-impulse-packages.yml
  title: ''
  type: SDKs
  url: packages/edge-impulse-packages.yml
- group: build
  href: https://artifacts.apis.io/edge-impulse/cli/edge-impulse-cli.yml
  title: ''
  type: CLI
  url: cli/edge-impulse-cli.yml
- group: agent
  href: https://artifacts.apis.io/edge-impulse/mcp/edge-impulse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/edge-impulse-mcp.yml
- group: build
  href: https://artifacts.apis.io/edge-impulse/mcp/edge-impulse-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/edge-impulse-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/edge-impulse/a2a/edge-impulse-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/edge-impulse-a2a.yml
- group: agent
  href: https://artifacts.apis.io/edge-impulse/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/edge-impulse/well-known/edge-impulse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/edge-impulse-well-known.yml
- group: design
  href: https://artifacts.apis.io/edge-impulse/conformance/edge-impulse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edge-impulse-conformance.yml
- group: auth
  href: https://artifacts.apis.io/edge-impulse/conformance/edge-impulse-conformance.yml
  title: ''
  type: Compliance
  url: conformance/edge-impulse-conformance.yml
- group: design
  href: https://artifacts.apis.io/edge-impulse/errors/edge-impulse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/edge-impulse-problem-types.yml
- group: design
  href: https://artifacts.apis.io/edge-impulse/lifecycle/edge-impulse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/edge-impulse-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://edgeimpulse.statuspage.io
- group: auth
  href: https://artifacts.apis.io/edge-impulse/scopes/edge-impulse-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/edge-impulse-scopes.yml
- group: design
  href: https://artifacts.apis.io/edge-impulse/conventions/edge-impulse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/edge-impulse-conventions.yml
- group: design
  href: https://artifacts.apis.io/edge-impulse/data-model/edge-impulse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/edge-impulse-data-model.yml
- group: docs
  href: https://artifacts.apis.io/edge-impulse/asyncapi/edge-impulse-remote-management-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/edge-impulse-remote-management-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/edge-impulse/asyncapi/edge-impulse-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/edge-impulse-webhooks.yml
- group: build
  title: ''
  type: Postman
  url: https://raw.githubusercontent.com/edgeimpulse/ei-agentic-claude/main/Edge%20Impulse%20API.postman_collection.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.edgeimpulse.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.edgeimpulse.com/apis/studio
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.edgeimpulse.com/knowledge/guides/getting-started-for-beginners
- group: operate
  title: ''
  type: Support
  url: https://forum.edgeimpulse.com/
- group: start
  title: ''
  type: Console
  url: https://docs.edgeimpulse.com/apis/studio#test-api-requests
- group: commercial
  title: ''
  type: Pricing
  url: https://www.edgeimpulse.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://studio.edgeimpulse.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edgeimpulse.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edgeimpulse.com/legal/privacy-policy
created: '2024-11-07'
description: 'Edge Impulse is the end-to-end edge AI MLOps platform for building datasets, training and optimizing machine learning models, and deploying them directly on device — from the smallest microcontrollers to gateways with the latest neural accelerators. The platform covers the whole workflow: sensor data collection and labeling, DSP feature engineering, model training with the EON Tuner and EON Compiler, hardware-aware profiling for latency, RAM and flash, and deployment as a C++ library, Arduino library, WebAssembly package, Docker container or prebuilt firmware. It is driven programmatically through three APIs — a 559-operation Studio API, an Ingestion API and a device Remote Management WebSocket — plus CLIs, Python/Node/Rust/Go SDKs and a first-party MCP server. Founded in 2019 by Zach Shelby and Jan Jongboom; acquired by Qualcomm Technologies in March 2025 and still operating under its own brand.'
finops:
- has_sources: true
  method: derived
  name: Edge Impulse Finops
  primary_unit: subscription
  service_category: ''
  slug: edge-impulse-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edge-impulse.png
layout: provider
mcp_servers:
- description: 'Edge Impulse ships MCP two ways, and they are different products. A REMOTE, anonymous documentation MCP endpoint answers tools/list today at https://docs.edgeimpulse.com/mcp (3 read-only docs tools). '
  name: Edge Impulse MCP Servers
  slug: edge-impulse-mcp-servers
modified: '2026-09-16'
name: Edge Impulse
nav: Providers
network: true
overview: 'Edge Impulse publishes 38 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Auth API, Canary API, and 35 more. Tagged areas include Artificial Intelligence, Machine Learning, Embedded Machine Learning, Edge AI, and MLOps.


  The Edge Impulse catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Edge Impulse''s developer surface includes authentication, documentation, engineering blog, FAQ, signup flow, CLI, API reference, and 49 more developer resources.'
plans:
- name: Edge Impulse Plans Pricing
  plan_count: 2
  slug: edge-impulse-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Edge Impulse Rate Limits
  slug: edge-impulse-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Edge Impulse API Rules
  rule_count: 55
  severity_counts:
    error: 35
    hint: 0
    info: 3
    warn: 17
  slug: edge-impulse-rules
scopes:
- name: Edge Impulse Scopes
  scope_count: 3
  slug: edge-impulse-scopes
  summary_line: 3 scopes · authorizationCode/implicit/password/clientCredentials
score:
  band: exemplar
  composite: 71.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 89.5
    contract_governance: 31.8
    contract_quality: 53.1
    developer_ergonomics: 90.5
    discoverability: 75.0
    operational_transparency: 39.5
  previous_composite: 71.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 41.7
      total: 36
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/edge-impulse/edge-impulse-2026-06-20T180450.png
security:
- kind: authentication
  name: Edge Impulse Authentication
  slug: edge-impulse-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Edge Impulse Domain Security
  slug: edge-impulse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Edge Impulse Vulnerability Disclosure
  slug: edge-impulse-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Edge Impulse Trust Center
  slug: edge-impulse-trust-center
  summary_line: SOC 2 Type II
skill_count: 7
skills:
- name: Edgeimpulse
  slug: edge-impulse-edgeimpulse
- name: ei-apply-flow-dryrun
  slug: edge-impulse-ei-apply-flow-dryrun
- name: ei-issue-triage
  slug: edge-impulse-ei-issue-triage
- name: ei-regenerate-clients
  slug: edge-impulse-ei-regenerate-clients
- name: ei-release-gate
  slug: edge-impulse-ei-release-gate
- name: ei-safe-ops
  slug: edge-impulse-ei-safe-ops
- name: edge-impulse-train-and-deploy
  slug: edge-impulse-train-and-deploy
slug: edge-impulse
tags:
- Artificial Intelligence
- Machine Learning
- Embedded Machine Learning
- Edge AI
- MLOps
- Computer Vision
- IoT
- Model Deployment
- Developer Tools
- Real-Time
- A2A
website: https://edgeimpulse.com/
---
