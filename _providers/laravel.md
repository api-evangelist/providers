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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.0
  scored_at: '2026-10-04'
api_count: 2
apis:
- description: The legacy v1 Laravel Forge REST API, documented at forge.laravel.com/api-documentation. Laravel has marked this version deprecated and states it will be discontinued on July 31, 2026; integrators are
  name: Laravel Forge API (Legacy v1)
  slug: forge-api-legacy
- description: The Envoyer REST API for zero-downtime PHP deployments. Create and manage projects, servers, environments, deployment hooks, deployments, collaborators and notifications. Bearer API key authentication
  name: Envoyer API
  slug: envoyer-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Applications API from Laravel — 3 operation(s) for applications.
  name: Laravel Applications API
  phrasing_intents:
  - id: public.applications.index
    intent: List my Cloud applications
    question: What applications does my Laravel Cloud organization have?
  - id: public.applications.store
    intent: Create an application from a repository
    question: How do I create a new application from my Git repository?
  - id: public.applications.show
    intent: Get an application
    question: What are the details of one of my applications?
  - id: public.applications.update
    intent: Update an application's settings
    question: Can I rename an application or change its slug?
  - id: public.applications.destroy
    intent: Delete an application and its environments
    question: What happens to the environments when I delete an application?
  - id: public.applications.avatar.store
    intent: Upload an application's avatar
    question: How do I add a logo or avatar to an application?
  - id: public.applications.avatar.destroy
    intent: Remove an application's avatar
    question: Can I remove the avatar from an application?
  phrasing_ops: 7
  slug: laravel-applications-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Background Processes API from Laravel — 5 operation(s) for background processes.
  name: Laravel Background Processes API
  phrasing_intents:
  - id: public.instances.background-processes.index
    intent: List background processes on a Cloud instance
    question: What background processes are running on one of my Laravel Cloud instances?
  - id: public.instances.background-processes.store
    intent: Add a background process to a Cloud instance
    question: How do I add a queue worker to a Cloud instance?
  - id: public.background-processes.show
    intent: Get a Cloud background process
    question: What command and process count does a Cloud background process use?
  - id: public.background-processes.update
    intent: Update a Cloud background process
    question: Can I change the number of processes a Cloud worker runs?
  - id: public.background-processes.destroy
    intent: Delete a Cloud background process
    question: How do I stop and remove a worker from a Laravel Cloud instance?
  - id: organizations.servers.background-processes.index
    intent: List background processes on a Forge server
    question: Which supervisor daemons are running on my Forge server?
  - id: organizations.servers.background-processes.store
    intent: Create a supervisor daemon on a Forge server
    question: How do I keep a command running permanently under supervisor on my server?
  - id: organizations.servers.background-processes.show
    intent: Get a background process on a Forge server
    question: What are the settings of one daemon on my Forge server?
  phrasing_ops: 11
  slug: laravel-background-processes-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Backups API from Laravel — 5 operation(s) for backups.
  name: Laravel Backups API
  phrasing_intents:
  - id: organizations.servers.database.backups.index
    intent: List database backup configurations on a server
    question: Which backup schedules are set up for my server's databases?
  - id: organizations.servers.database.backups.store
    intent: Schedule database backups on a server
    question: How do I schedule nightly database backups to my storage provider?
  - id: organizations.servers.database.backups.show
    intent: Get a database backup configuration
    question: What schedule and retention does a particular backup configuration use?
  - id: organizations.servers.database.backups.update
    intent: Change a database backup schedule
    question: Can I change how often an existing backup configuration runs?
  - id: organizations.servers.database.backups.destroy
    intent: Delete a database backup configuration
    question: How do I stop a scheduled database backup permanently?
  - id: organizations.servers.database.backups.instances.index
    intent: List backups taken by a backup configuration
    question: Which database backups have actually been taken under a schedule?
  - id: organizations.servers.database.backups.instances.store
    intent: Run a database backup now
    question: Can I take a database backup right now instead of waiting for the schedule?
  - id: organizations.servers.database.backups.instances.show
    intent: Get one database backup
    question: Did a specific backup run succeed?
  phrasing_ops: 10
  slug: laravel-backups-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Bucket Keys API from Laravel — 2 operation(s) for bucket keys.
  name: Laravel Bucket Keys API
  phrasing_intents:
  - id: public.buckets.keys.index
    intent: List access keys for a storage bucket
    question: Which access keys exist for an object storage bucket?
  - id: public.buckets.keys.store
    intent: Create an access key for a storage bucket
    question: How do I create credentials for an object storage bucket?
  - id: public.bucket-keys.show
    intent: Get a bucket access key
    question: What permission does a particular bucket key have?
  - id: public.bucket-keys.update
    intent: Rename a bucket access key
    question: Can I rename an existing object storage key?
  - id: public.bucket-keys.destroy
    intent: Delete a bucket access key
    question: How do I revoke an object storage key?
  phrasing_ops: 5
  slug: laravel-bucket-keys-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Caches API from Laravel — 4 operation(s) for caches.
  name: Laravel Caches API
  phrasing_intents:
  - id: public.caches.types
    intent: List available cache types and options
    question: What kinds of cache can I create on Laravel Cloud?
  - id: public.caches.index
    intent: List my organization's caches
    question: Which caches does my organization have running?
  - id: public.caches.store
    intent: Create a cache
    question: How do I spin up a new Redis-compatible cache in a region?
  - id: public.caches.show
    intent: Get a cache's details
    question: What size and region is a specific cache in?
  - id: public.caches.update
    intent: Resize or reconfigure a cache
    question: Can I resize an existing cache without recreating it?
  - id: public.caches.destroy
    intent: Delete a cache
    question: How do I tear down a cache I no longer need?
  - id: public.caches.metrics
    intent: Get usage metrics for a cache
    question: How much memory and traffic is my cache using?
  phrasing_ops: 7
  slug: laravel-caches-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Commands API from Laravel — 5 operation(s) for commands.
  name: Laravel Commands API
  phrasing_intents:
  - id: public.environments.commands.index
    intent: List commands run on a Cloud environment
    question: Which commands have been run against my Laravel Cloud environment?
  - id: public.environments.commands.store
    intent: Run a command on a Cloud environment
    question: How do I run php artisan migrate on a cloud environment?
  - id: public.commands.show
    intent: Get a Cloud command run's details
    question: Did the cloud command I ran finish successfully?
  - id: organizations.servers.sites.commands.index
    intent: List command runs on a Forge site
    question: Which commands have been run on my Forge site?
  - id: organizations.servers.sites.commands.store
    intent: Run a command on a Forge site
    question: How do I run an artisan command in a site's directory on my server?
  - id: organizations.servers.sites.commands.show
    intent: Get one command run on a Forge site
    question: What status did a specific site command finish with?
  - id: organizations.servers.sites.commands.destroy
    intent: Delete a site command from history
    question: Can I clear a command I ran from a site's command history?
  - id: organizations.servers.sites.commands.output.show
    intent: Read the output of a site command run
    question: What did a command print when it ran on my site?
  phrasing_ops: 8
  slug: laravel-commands-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Database Clusters API from Laravel — 4 operation(s) for database clusters.
  name: Laravel Database Clusters API
  phrasing_intents:
  - id: public.databases.types
    intent: List available database types
    question: What kinds of managed databases can I create in Laravel Cloud?
  - id: public.databases.clusters.index
    intent: List my database clusters
    question: Which database clusters does my organization have?
  - id: public.databases.clusters.store
    intent: Create a database cluster
    question: How do I create a managed database cluster?
  - id: public.databases.clusters.show
    intent: Get a database cluster
    question: What is the status and configuration of a database cluster?
  - id: public.databases.clusters.update
    intent: Change a database cluster's configuration
    question: Can I resize or reconfigure an existing database cluster?
  - id: public.databases.clusters.destroy
    intent: Delete a database cluster
    question: How do I delete a database cluster?
  - id: public.databases.clusters.metrics
    intent: Get a database cluster's metrics
    question: How busy is my database cluster?
  phrasing_ops: 7
  slug: laravel-database-clusters-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Database Restores API from Laravel — 1 operation(s) for database restores.
  name: Laravel Database Restores API
  phrasing_intents:
  - id: public.databases.clusters.restore
    intent: Restore a database cluster to a point in time
    question: How do I restore my database to how it was an hour ago?
  phrasing_ops: 1
  slug: laravel-database-restores-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Database Snapshots API from Laravel — 2 operation(s) for database snapshots.
  name: Laravel Database Snapshots API
  phrasing_intents:
  - id: public.databases.clusters.snapshots.index
    intent: List snapshots of a database cluster
    question: Which snapshots exist for my database cluster?
  - id: public.databases.clusters.snapshots.store
    intent: Take a manual database cluster snapshot
    question: How do I snapshot my database cluster before a big change?
  - id: public.database-snapshots.show
    intent: Get a database snapshot
    question: What is the status of a particular database snapshot?
  - id: public.database-snapshots.destroy
    intent: Delete a database snapshot
    question: How do I delete an old database snapshot?
  phrasing_ops: 4
  slug: laravel-database-snapshots-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Databases API from Laravel — 8 operation(s) for databases.
  name: Laravel Databases API
  phrasing_intents:
  - id: public.databases.clusters.databases.index
    intent: List databases in a Cloud database cluster
    question: Which databases live inside my Laravel Cloud database cluster?
  - id: public.databases.clusters.databases.store
    intent: Create a database in a Cloud cluster
    question: How do I add a new database to an existing managed database cluster?
  - id: public.databases.clusters.databases.show
    intent: Get a database in a Cloud cluster
    question: What are the details of one database inside my cloud cluster?
  - id: public.databases.clusters.databases.destroy
    intent: Delete a database from a Cloud cluster
    question: Can I drop one database from a cloud cluster without deleting the whole cluster?
  - id: organizations.servers.database.schemas.index
    intent: List database schemas on a Forge server
    question: Which databases exist on my Forge server?
  - id: organizations.servers.database.schemas.store
    intent: Create a database schema on a server
    question: How do I create a new MySQL or Postgres database on my server?
  - id: organizations.servers.database.schemas.show
    intent: Get a database schema on a server
    question: What is the status of a specific database on my server?
  - id: organizations.servers.database.schemas.destroy
    intent: Delete a database schema from a server
    question: How do I remove a database schema I no longer need from my server?
  phrasing_ops: 15
  slug: laravel-databases-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Databases (Legacy) API from Laravel — 2 operation(s) for databases (legacy).
  name: Laravel Databases (Legacy) API
  phrasing_intents:
  - id: public.databases.deprecated.index
    intent: List databases (deprecated endpoint)
    question: Can I still list my databases with the older deprecated /databases endpoint?
  - id: public.databases.deprecated.store
    intent: Create a database (deprecated endpoint)
    question: Is the legacy POST /databases endpoint still usable for creating a database?
  - id: public.databases.deprecated.show
    intent: Get a database (deprecated endpoint)
    question: Can I look up a database through the deprecated single-database endpoint?
  - id: public.databases.deprecated.update
    intent: Update a database's config (deprecated endpoint)
    question: Can I change a database's configuration with the deprecated update call?
  - id: public.databases.deprecated.destroy
    intent: Delete a database (deprecated endpoint)
    question: Can I still delete a database through the deprecated endpoint?
  phrasing_ops: 5
  slug: laravel-databases-legacy-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Dedicated Clusters API from Laravel — 1 operation(s) for dedicated clusters.
  name: Laravel Dedicated Clusters API
  phrasing_intents:
  - id: public.dedicated-clusters.index
    intent: List dedicated clusters
    question: Which dedicated clusters does my Laravel Cloud organization have?
  phrasing_ops: 1
  slug: laravel-dedicated-clusters-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Deployments API from Laravel — 13 operation(s) for deployments.
  name: Laravel Deployments API
  phrasing_intents:
  - id: public.environments.deployments.index
    intent: List deployments for a Cloud environment
    question: Which deployments have run against my Laravel Cloud environment?
  - id: public.environments.deployments.store
    intent: Deploy a Cloud environment
    question: How do I kick off a new deployment of a cloud environment?
  - id: public.deployments.show
    intent: Get a Cloud deployment's details
    question: What is the status of a specific cloud deployment I started?
  - id: public.deployments.logs
    intent: Read build and deploy logs for a Cloud deployment
    question: Where can I see the build logs for a cloud deployment that failed?
  - id: organizations.servers.sites.webhooks.index
    intent: List deployment webhooks for a Forge site
    question: Which webhook URLs get notified when my Forge site deploys?
  - id: organizations.servers.sites.webhooks.store
    intent: Add a deployment webhook to a site
    question: How can I get pinged at my own URL every time a site finishes deploying?
  - id: organizations.servers.sites.webhooks.show
    intent: Get one deployment webhook on a site
    question: What URL does a particular site deployment webhook point to?
  - id: organizations.servers.sites.webhooks.destroy
    intent: Remove a deployment webhook from a site
    question: How do I stop a site from calling an old webhook URL after deploys?
  phrasing_ops: 23
  slug: laravel-deployments-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Domains API from Laravel — 3 operation(s) for domains.
  name: Laravel Domains API
  phrasing_intents:
  - id: public.environments.domains.index
    intent: List domains attached to an environment
    question: Which custom domains point at my Laravel Cloud environment?
  - id: public.environments.domains.store
    intent: Add a custom domain to an environment
    question: How do I attach my own domain to a cloud environment?
  - id: public.domains.show
    intent: Get a domain's DNS and SSL status
    question: Which DNS records do I still need to add for my domain?
  - id: public.domains.update
    intent: Change a domain's verification method
    question: Can I switch how my domain is verified after adding it?
  - id: public.domains.destroy
    intent: Remove a domain from an environment
    question: How do I detach a domain I'm no longer using?
  - id: public.domains.verify
    intent: Verify a domain's DNS records
    question: I added the DNS records — how do I check they're set up correctly?
  phrasing_ops: 6
  slug: laravel-domains-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Environments API from Laravel — 9 operation(s) for environments.
  name: Laravel Environments API
  phrasing_intents:
  - id: public.applications.environments.index
    intent: List an application's environments
    question: Which environments does my Laravel Cloud application have?
  - id: public.applications.environments.store
    intent: Create an environment for an application
    question: How do I add a staging environment to my application?
  - id: public.environments.logs.index
    intent: Search an environment's logs
    question: Where can I read the application logs for an environment over a time range?
  - id: public.environments.show
    intent: Get an environment's details
    question: What are the settings of a specific environment?
  - id: public.environments.update
    intent: Change an environment's settings
    question: How do I change the branch or PHP version an environment deploys?
  - id: public.environments.destroy
    intent: Delete an environment
    question: How do I delete an environment I no longer need?
  - id: public.environments.start
    intent: Start an environment and deploy
    question: How do I start a stopped environment?
  - id: public.environments.stop
    intent: Stop an environment
    question: How do I stop an environment that is running?
  phrasing_ops: 12
  slug: laravel-environments-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Firewall Rules API from Laravel — 2 operation(s) for firewall rules.
  name: Laravel Firewall Rules API
  phrasing_intents:
  - id: organizations.servers.firewall-rules.index
    intent: List a server's firewall rules
    question: Which ports are open in my server's firewall?
  - id: organizations.servers.firewall-rules.store
    intent: Open or block a port on a server
    question: How do I open a port on my server's firewall?
  - id: organizations.servers.firewall-rules.show
    intent: Get one firewall rule on a server
    question: Which port and IP does a specific firewall rule cover?
  - id: organizations.servers.firewall-rules.destroy
    intent: Remove a firewall rule from a server
    question: How do I close a port I opened earlier?
  phrasing_ops: 4
  slug: laravel-firewall-rules-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Instances API from Laravel — 10 operation(s) for instances.
  name: Laravel Instances API
  phrasing_intents:
  - id: public.environments.instances.index
    intent: List an environment's instances
    question: What compute instances are running in one of my Laravel Cloud environments?
  - id: public.environments.instances.store
    intent: Create an instance in an environment
    question: How do I add a worker or managed queue instance to an environment?
  - id: public.instances.sizes
    intent: List available instance sizes
    question: What instance sizes can I choose from, grouped by category?
  - id: public.instances.show
    intent: Get an instance's details
    question: What size and replica settings does one of my instances have?
  - id: public.instances.update
    intent: Resize or reconfigure an instance
    question: Can I change the size or replica limits of an existing instance?
  - id: public.instances.destroy
    intent: Delete an instance
    question: How do I remove an instance I no longer need from my environment?
  - id: public.instances.pause
    intent: Pause a managed queue
    question: Can I stop workers from picking up jobs without losing what is queued?
  - id: public.instances.resume
    intent: Resume a paused managed queue
    question: How do I start a paused queue processing jobs again?
  phrasing_ops: 13
  slug: laravel-instances-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Integrations API from Laravel — 7 operation(s) for integrations.
  name: Laravel Integrations API
  phrasing_intents:
  - id: organizations.servers.sites.integrations.horizon.show
    intent: Check whether Horizon is enabled on a site
    question: Is Laravel Horizon set up to run the queue workers on my site?
  - id: organizations.servers.sites.integrations.horizon.store
    intent: Enable Laravel Horizon on a site
    question: How do I turn on Horizon so my site's Redis queues are managed?
  - id: organizations.servers.sites.integrations.horizon.destroy
    intent: Disable Laravel Horizon on a site
    question: Can I remove Horizon from a site that no longer uses queues?
  - id: organizations.servers.sites.integrations.octane.show
    intent: Check whether Octane is enabled on a site
    question: Is my site being served by Laravel Octane?
  - id: organizations.servers.sites.integrations.octane.store
    intent: Enable Laravel Octane on a site
    question: Can I run my site on Octane with a specific port and server engine?
  - id: organizations.servers.sites.integrations.octane.destroy
    intent: Disable Laravel Octane on a site
    question: How do I move a site off Octane back to regular PHP-FPM serving?
  - id: organizations.servers.sites.integrations.reverb.show
    intent: Check whether Reverb is enabled on a site
    question: Is the Reverb WebSocket server running for my site?
  - id: organizations.servers.sites.integrations.reverb.store
    intent: Enable Laravel Reverb on a site
    question: How do I set up Reverb WebSockets on a site with my own host, port and connection limit?
  phrasing_ops: 20
  slug: laravel-integrations-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Logs API from Laravel — 1 operation(s) for logs.
  name: Laravel Logs API
  phrasing_intents:
  - id: organizations.servers.logs.show
    intent: Read a server log file
    question: Can I read a server-level log file, such as the PHP or MySQL log?
  - id: organizations.servers.logs.destroy
    intent: Clear a server log file
    question: How do I clear out a large log file on my server?
  phrasing_ops: 2
  slug: laravel-logs-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Meta API from Laravel — 2 operation(s) for meta.
  name: Laravel Meta API
  phrasing_intents:
  - id: public.meta.organization
    intent: Get my current organization
    question: Which Laravel Cloud organization is my API token tied to?
  - id: public.meta.regions
    intent: List available cloud regions
    question: Which regions can I deploy to in Laravel Cloud?
  phrasing_ops: 2
  slug: laravel-meta-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Monitors API from Laravel — 2 operation(s) for monitors.
  name: Laravel Monitors API
  phrasing_intents:
  - id: organizations.servers.monitors.index
    intent: List a server's monitors
    question: What resource monitors are set up on my server?
  - id: organizations.servers.monitors.store
    intent: Create a server resource monitor
    question: How do I get an alert when my server's disk or CPU usage crosses a threshold?
  - id: organizations.servers.monitors.show
    intent: Get a server monitor
    question: What threshold and state does one server monitor have?
  - id: organizations.servers.monitors.destroy
    intent: Delete a server monitor
    question: How do I stop a monitor from sending alerts by removing it?
  phrasing_ops: 4
  slug: laravel-monitors-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Nginx API from Laravel — 2 operation(s) for nginx.
  name: Laravel Nginx API
  phrasing_intents:
  - id: organizations.servers.nginx.templates.index
    intent: List a server's Nginx templates
    question: Which Nginx templates are saved on my server?
  - id: organizations.servers.nginx.templates.store
    intent: Create an Nginx template on a server
    question: How do I save a custom Nginx config as a template for new sites?
  - id: organizations.servers.nginx.templates.show
    intent: Get an Nginx template
    question: What does one of my server's Nginx templates contain?
  - id: organizations.servers.nginx.templates.update
    intent: Edit an Nginx template
    question: How do I change an existing Nginx template on my server?
  - id: organizations.servers.nginx.templates.destroy
    intent: Delete an Nginx template
    question: How do I remove an Nginx template I no longer use?
  phrasing_ops: 5
  slug: laravel-nginx-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Object Storage Buckets API from Laravel — 2 operation(s) for object storage buckets.
  name: Laravel Object Storage Buckets API
  phrasing_intents:
  - id: public.buckets.index
    intent: List object storage buckets
    question: Which object storage buckets does my organization have?
  - id: public.buckets.store
    intent: Create an object storage bucket
    question: How do I create a storage bucket for user uploads?
  - id: public.buckets.show
    intent: Get an object storage bucket
    question: What visibility and status does a specific bucket have?
  - id: public.buckets.update
    intent: Change a bucket's visibility or CORS
    question: Can I make an existing private bucket public?
  - id: public.buckets.destroy
    intent: Delete an object storage bucket
    question: How do I delete a storage bucket I no longer need?
  phrasing_ops: 5
  slug: laravel-object-storage-buckets-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Organizations API from Laravel — 6 operation(s) for organizations.
  name: Laravel Organizations API
  phrasing_intents:
  - id: organizations.index
    intent: List my organizations
    question: Which Forge organizations does my account belong to?
  - id: organizations.show
    intent: Get an organization
    question: What are the details of one organization I belong to?
  - id: organizations.server-credentials.index
    intent: List an organization's server provider credentials
    question: Which cloud provider credentials are linked to my organization?
  - id: organizations.server-credentials.show
    intent: Get a server provider credential
    question: Which provider is a particular server credential for?
  - id: organizations.server-credentials.vpcs.store
    intent: Create a VPC with a provider credential
    question: How do I create a new private network in a region for my servers?
  - id: organizations.server-credentials.vpcs.index
    intent: List VPCs for a provider credential in a region
    question: What private networks exist in a region for my cloud provider credential?
  - id: organizations.server-credentials.vpcs.show
    intent: Get a VPC for a provider credential
    question: What are the details of one VPC in my provider account?
  phrasing_ops: 7
  slug: laravel-organizations-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Providers API from Laravel — 8 operation(s) for providers.
  name: Laravel Providers API
  phrasing_intents:
  - id: providers.index
    intent: List supported server providers
    question: Which cloud providers can Forge create servers on?
  - id: providers.show
    intent: Get a server provider
    question: What details are available for one server provider?
  - id: providers.sizes.index
    intent: List a provider's server sizes
    question: What server sizes can I choose from at a provider?
  - id: providers.sizes.show
    intent: Get a provider server size
    question: How much CPU and memory does a provider size have?
  - id: providers.regions.index
    intent: List a provider's regions
    question: Which regions can I deploy a server into at a provider?
  - id: providers.regions.show
    intent: Get a provider region
    question: What details are there about a specific provider region?
  - id: providers.regions.sizes.index
    intent: List server sizes available in a region
    question: Which server sizes are offered in one particular region?
  - id: providers.regions.sizes.show
    intent: Get a server size within a region
    question: Is a specific server size offered in a given region?
  phrasing_ops: 8
  slug: laravel-providers-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Recipes API from Laravel — 9 operation(s) for recipes.
  name: Laravel Recipes API
  phrasing_intents:
  - id: organizations.recipes.index
    intent: List my organization's recipes
    question: Which bash recipes has my organization saved in Forge?
  - id: organization.recipes.store
    intent: Create a reusable server recipe
    question: How do I save a bash script as a recipe I can run on many servers?
  - id: organizations.recipes.show
    intent: Get one of my recipes
    question: What script does a particular recipe of ours contain?
  - id: organizations.recipes.update
    intent: Edit a saved recipe
    question: Can I change the script inside an existing recipe?
  - id: organizations.recipes.destroy
    intent: Delete a saved recipe
    question: How do I remove a recipe we no longer use?
  - id: organizations.recipes.runs.index
    intent: List past runs of a recipe
    question: Where can I see every time a recipe was run?
  - id: organizations.recipes.runs.store
    intent: Run one of my recipes on servers
    question: How do I run our custom recipe across several servers at once?
  - id: organizations.recipes.runs.show
    intent: Get the result of a recipe run
    question: What was the output of one specific recipe run?
  phrasing_ops: 14
  slug: laravel-recipes-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Redirect Rules API from Laravel — 2 operation(s) for redirect rules.
  name: Laravel Redirect Rules API
  phrasing_intents:
  - id: organizations.servers.sites.redirect-rules.index
    intent: List a site's redirect rules
    question: Which redirects are configured on my site?
  - id: organizations.servers.sites.redirect-rules.store
    intent: Add a redirect rule to a site
    question: How do I redirect an old URL path to a new one on my site?
  - id: organizations.servers.sites.redirect-rules.show
    intent: Get a site redirect rule
    question: What are the details of one redirect rule on my site?
  - id: organizations.servers.sites.redirect-rules.destroy
    intent: Remove a site redirect rule
    question: How do I delete a redirect from my site?
  phrasing_ops: 4
  slug: laravel-redirect-rules-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Roles API from Laravel — 7 operation(s) for roles.
  name: Laravel Roles API
  phrasing_intents:
  - id: predefined-roles.index
    intent: List Forge's predefined roles
    question: What built-in roles are available out of the box?
  - id: predefined-roles.show
    intent: Get a predefined role
    question: What permissions does a specific built-in role grant?
  - id: permissions.index
    intent: List all available permissions
    question: Which permissions can I assign to a role?
  - id: permissions.show
    intent: Get a permission
    question: What does a specific permission allow?
  - id: organizations.roles.store
    intent: Create a custom role
    question: How do I create a custom role for my organization?
  - id: organizations.roles.index
    intent: List my organization's custom roles
    question: What roles has my organization defined?
  - id: organizations.roles.show
    intent: Get one of my organization's roles
    question: What are the details of a custom role in my organization?
  - id: organizations.roles.update
    intent: Edit a custom role
    question: How do I change the permissions on an existing role?
  phrasing_ops: 10
  slug: laravel-roles-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Scheduled Jobs API from Laravel — 6 operation(s) for scheduled jobs.
  name: Laravel Scheduled Jobs API
  phrasing_intents:
  - id: organizations.servers.scheduled-jobs.index
    intent: List a server's scheduled jobs
    question: What cron jobs are scheduled on my server?
  - id: organizations.servers.scheduled-jobs.store
    intent: Schedule a cron job on a server
    question: How do I add a cron job to a server that isn't tied to a site?
  - id: organizations.servers.scheduled-jobs.show
    intent: Get a server scheduled job
    question: What command and schedule does one server cron job have?
  - id: organizations.servers.scheduled-jobs.destroy
    intent: Delete a server scheduled job
    question: How do I remove a cron job from my server?
  - id: organizations.servers.scheduled-jobs.outputs.show
    intent: Get a server scheduled job's output
    question: What did my server cron job print the last time it ran?
  - id: organizations.servers.sites.scheduled-jobs.index
    intent: List a site's scheduled jobs
    question: Which scheduled jobs belong to one particular site?
  - id: organizations.servers.sites.scheduled-jobs.store
    intent: Schedule a cron job for a site
    question: How do I add a scheduled task that belongs to a specific site?
  - id: organizations.servers.sites.scheduled-jobs.show
    intent: Get a site scheduled job
    question: What schedule is a particular site cron job using?
  phrasing_ops: 10
  slug: laravel-scheduled-jobs-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Security Rules API from Laravel — 2 operation(s) for security rules.
  name: Laravel Security Rules API
  phrasing_intents:
  - id: organizations.servers.sites.security-rules.index
    intent: List a site's password protection rules
    question: Which paths on my site are password protected?
  - id: organizations.servers.sites.security-rules.store
    intent: Password-protect a path on a site
    question: How do I put basic auth in front of my staging site?
  - id: organizations.servers.sites.security-rules.show
    intent: Get a site security rule
    question: What path and users does one security rule protect?
  - id: organizations.servers.sites.security-rules.update
    intent: Update a site security rule
    question: Can I change the credentials on an existing password protection rule?
  - id: organizations.servers.sites.security-rules.destroy
    intent: Remove a site security rule
    question: How do I take password protection off a site?
  phrasing_ops: 5
  slug: laravel-security-rules-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Server Credentials API from Laravel — 2 operation(s) for server credentials.
  name: Laravel Server Credentials API
  phrasing_intents:
  - id: organizations.teams.server-credentials.index
    intent: List server credentials shared with a team
    question: Which server provider credentials can my team use?
  - id: organizations.teams.server-credentials.store
    intent: Share a server credential with a team
    question: How do I let a team provision servers with one of my provider credentials?
  - id: organizations.teams.server-credentials.destroy
    intent: Unshare a server credential from a team
    question: Can I stop a team from using one of my server credentials?
  phrasing_ops: 3
  slug: laravel-server-credentials-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Servers API from Laravel — 28 operation(s) for servers.
  name: Laravel Servers API
  phrasing_intents:
  - id: organizations.servers.index
    intent: List an organization's Forge servers
    question: Which servers does my Forge organization have running?
  - id: organizations.servers.store
    intent: Provision a new server
    question: How do I provision a new server through Laravel Forge?
  - id: organizations.servers.archives.index
    intent: List archived servers
    question: Which of my servers have been archived?
  - id: organizations.servers.archives.store
    intent: Archive a server
    question: Can I archive a server instead of deleting it?
  - id: organizations.servers.archives.destroy
    intent: Unarchive a server
    question: How do I bring an archived server back into use?
  - id: organizations.servers.background-processes.actions.store
    intent: Restart, stop or start a server background process
    question: How do I restart a daemon running at the server level?
  - id: organizations.servers.actions.store
    intent: Reboot or power-cycle a server
    question: How do I reboot a whole server from the API?
  - id: organizations.servers.services.nginx.actions.store
    intent: Reboot or stop Nginx on a server
    question: How do I restart Nginx on one of my servers?
  phrasing_ops: 46
  slug: laravel-servers-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Sites API from Laravel — 30 operation(s) for sites.
  name: Laravel Sites API
  phrasing_intents:
  - id: sites.index
    intent: List every site my token can access
    question: Can I see every Forge site my API token has access to, across all organizations?
  - id: organizations.sites.index
    intent: List all sites in an organization
    question: What sites does one organization have across all of its servers?
  - id: organizations.sites.show
    intent: Get a site by organization and site ID
    question: Can I look up a site by its ID without knowing which server it lives on?
  - id: organizations.servers.sites.index
    intent: List the sites hosted on a server
    question: Which sites are hosted on a particular server?
  - id: organizations.servers.sites.store
    intent: Create a site on a server
    question: How do I add a new site to one of my Forge servers?
  - id: organizations.servers.sites.storeOnBalancer
    intent: Create a site on a load balancer
    question: Can I set up a site on a load balancer server rather than an app server?
  - id: organizations.servers.sites.update
    intent: Update an existing site's settings
    question: Can I change the PHP version an existing site runs?
  - id: organizations.servers.sites.destroy
    intent: Delete a site from a server
    question: How do I remove a site from a server entirely?
  phrasing_ops: 54
  slug: laravel-sites-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The SSH Keys API from Laravel — 3 operation(s) for ssh keys.
  name: Laravel SSH Keys API
  phrasing_intents:
  - id: organizations.servers.ssh-keys.index
    intent: List SSH keys authorized on a server
    question: Which SSH keys can log in to my server?
  - id: organizations.servers.ssh-keys.store
    intent: Add an SSH key to a server
    question: How do I give a teammate SSH access to a server?
  - id: organizations.servers.ssh-keys.show
    intent: Get an SSH key on a server
    question: What are the details of one SSH key installed on a server?
  - id: organizations.servers.ssh-keys.destroy
    intent: Remove an SSH key from a server
    question: How do I revoke someone's SSH access to a server?
  - id: organizations.servers.key.show
    intent: Get a server's own public SSH key
    question: What is my server's public key so I can add it to my git host as a deploy key?
  - id: organizations.servers.key.update
    intent: Regenerate a server's SSH key pair
    question: How do I rotate a server's own SSH key pair?
  phrasing_ops: 6
  slug: laravel-ssh-keys-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Storage Providers API from Laravel — 2 operation(s) for storage providers.
  name: Laravel Storage Providers API
  phrasing_intents:
  - id: organizations.storage-providers.index
    intent: List backup storage providers
    question: Which storage destinations has my organization configured?
  - id: organizations.storage-providers.store
    intent: Add a storage provider
    question: How do I connect an S3-compatible bucket as a storage provider?
  - id: organizations.storage-providers.show
    intent: Get a storage provider
    question: What bucket and region does one of our storage providers point to?
  - id: organizations.storage-providers.update
    intent: Change a storage provider's settings
    question: How do I rotate the access keys on a storage provider?
  - id: organizations.storage-providers.destroy
    intent: Delete a storage provider
    question: How do I remove a storage provider we no longer use?
  phrasing_ops: 5
  slug: laravel-storage-providers-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Teams API from Laravel — 6 operation(s) for teams.
  name: Laravel Teams API
  phrasing_intents:
  - id: organizations.teams.index
    intent: List an organization's teams
    question: Which teams exist in my Forge organization?
  - id: organizations.teams.store
    intent: Create a team in an organization
    question: How do I set up a new team for a group of developers?
  - id: organizations.teams.show
    intent: Get a team's details
    question: What are the details of one specific team?
  - id: organizations.teams.update
    intent: Rename a team or change its users
    question: Can I rename an existing team?
  - id: organizations.teams.destroy
    intent: Delete a team
    question: How do I delete a team we no longer use?
  - id: organizations.teams.members.index
    intent: List a team's members
    question: Who is on a particular team?
  - id: organizations.teams.members.show
    intent: Get one team member
    question: What role does a specific person have on a team?
  - id: organizations.teams.members.destroy
    intent: Remove a member from a team
    question: Can I take someone off a team when they leave the project?
  phrasing_ops: 13
  slug: laravel-teams-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The Usage API from Laravel — 1 operation(s) for usage.
  name: Laravel Usage API
  phrasing_intents:
  - id: public.usage
    intent: Get billing and usage data
    question: How much has my organization spent on Laravel Cloud this period?
  phrasing_ops: 1
  slug: laravel-usage-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The User API from Laravel — 2 operation(s) for user.
  name: Laravel User API
  phrasing_intents:
  - id: user.show
    intent: Get the authenticated user via /user
    question: Which account is my API token authenticated as, using the /user endpoint?
  - id: me
    intent: Get the authenticated user via /me
    question: Who am I logged in as, according to the /me endpoint?
  phrasing_ops: 2
  slug: laravel-user-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The WebSocket Applications API from Laravel — 3 operation(s) for websocket applications.
  name: Laravel WebSocket Applications API
  phrasing_intents:
  - id: public.websocket-servers.applications.index
    intent: List applications on a WebSocket cluster
    question: Which WebSocket applications run on one of my WebSocket clusters?
  - id: public.websocket-servers.applications.store
    intent: Create a WebSocket application
    question: How do I create a new WebSocket application on my cluster?
  - id: public.websocket-applications.show
    intent: Get a WebSocket application and its credentials
    question: Where do I find the key and secret for my WebSocket application?
  - id: public.websocket-applications.update
    intent: Update a WebSocket application's settings
    question: Can I change the allowed origins of an existing WebSocket app?
  - id: public.websocket-applications.destroy
    intent: Delete a WebSocket application
    question: How do I delete a WebSocket application I no longer use?
  - id: public.websocket-applications.metrics
    intent: Get a WebSocket application's metrics
    question: How much traffic is my WebSocket application handling?
  phrasing_ops: 6
  slug: laravel-websocket-applications-api
- baseURL: https://forge.laravel.com/api
  baseurl_source: declared
  description: The WebSocket Clusters API from Laravel — 3 operation(s) for websocket clusters.
  name: Laravel WebSocket Clusters API
  phrasing_intents:
  - id: public.websocket-servers.index
    intent: List WebSocket clusters
    question: Which WebSocket clusters does my organization run?
  - id: public.websocket-servers.store
    intent: Create a WebSocket cluster
    question: How do I create a managed WebSocket cluster for real-time features?
  - id: public.websocket-servers.show
    intent: Get a WebSocket cluster's details
    question: What connection limit and region does one WebSocket cluster have?
  - id: public.websocket-servers.update
    intent: Rename or resize a WebSocket cluster
    question: Can I raise the connection limit on an existing WebSocket cluster?
  - id: public.websocket-servers.destroy
    intent: Delete a WebSocket cluster
    question: What happens to its applications when I delete a WebSocket cluster?
  - id: public.websocket-servers.metrics
    intent: Get metrics for a WebSocket cluster
    question: How many connections and messages is my WebSocket cluster handling?
  phrasing_ops: 6
  slug: laravel-websocket-clusters-api
artifact_total: 133
asyncapis:
- description: ''
  name: Laravel Webhooks
  slug: laravel-webhooks
collections:
- collection_type: postman
  name: Laravel Cloud Applications API
  slug: postman-laravel-applications-api
- collection_type: postman
  name: Laravel Cloud Applications Background Processes API
  slug: postman-laravel-background-processes-api
- collection_type: postman
  name: Laravel Cloud Applications Backups API
  slug: postman-laravel-backups-api
- collection_type: postman
  name: Laravel Cloud Applications Bucket Keys API
  slug: postman-laravel-bucket-keys-api
- collection_type: postman
  name: Laravel Cloud Applications Caches API
  slug: postman-laravel-caches-api
- collection_type: postman
  name: Laravel Cloud Applications Commands API
  slug: postman-laravel-commands-api
- collection_type: postman
  name: Laravel Cloud Applications Database Clusters API
  slug: postman-laravel-database-clusters-api
- collection_type: postman
  name: Laravel Cloud Applications Database Restores API
  slug: postman-laravel-database-restores-api
- collection_type: postman
  name: Laravel Cloud Applications Database Snapshots API
  slug: postman-laravel-database-snapshots-api
- collection_type: postman
  name: Laravel Cloud Applications Databases API
  slug: postman-laravel-databases-api
- collection_type: postman
  name: Laravel Cloud Applications Databases (Legacy) API
  slug: postman-laravel-databases-legacy-api
- collection_type: postman
  name: Laravel Cloud Applications Dedicated Clusters API
  slug: postman-laravel-dedicated-clusters-api
- collection_type: postman
  name: Laravel Cloud Applications Deployments API
  slug: postman-laravel-deployments-api
- collection_type: postman
  name: Laravel Cloud Applications Domains API
  slug: postman-laravel-domains-api
- collection_type: postman
  name: Laravel Cloud Applications Environments API
  slug: postman-laravel-environments-api
- collection_type: postman
  name: Laravel Cloud Applications Firewall Rules API
  slug: postman-laravel-firewall-rules-api
- collection_type: postman
  name: Laravel Cloud Applications Instances API
  slug: postman-laravel-instances-api
- collection_type: postman
  name: Laravel Cloud Applications Integrations API
  slug: postman-laravel-integrations-api
- collection_type: postman
  name: Laravel Cloud Applications Logs API
  slug: postman-laravel-logs-api
- collection_type: postman
  name: Laravel Cloud Applications Meta API
  slug: postman-laravel-meta-api
- collection_type: postman
  name: Laravel Cloud Applications Monitors API
  slug: postman-laravel-monitors-api
- collection_type: postman
  name: Laravel Cloud Applications Nginx API
  slug: postman-laravel-nginx-api
- collection_type: postman
  name: Laravel Cloud Applications Object Storage Buckets API
  slug: postman-laravel-object-storage-buckets-api
- collection_type: postman
  name: Laravel Cloud Applications Organizations API
  slug: postman-laravel-organizations-api
- collection_type: postman
  name: Laravel Cloud Applications Providers API
  slug: postman-laravel-providers-api
- collection_type: postman
  name: Laravel Cloud Applications Recipes API
  slug: postman-laravel-recipes-api
- collection_type: postman
  name: Laravel Cloud Applications Redirect Rules API
  slug: postman-laravel-redirect-rules-api
- collection_type: postman
  name: Laravel Cloud Applications Roles API
  slug: postman-laravel-roles-api
- collection_type: postman
  name: Laravel Cloud Applications Scheduled Jobs API
  slug: postman-laravel-scheduled-jobs-api
- collection_type: postman
  name: Laravel Cloud Applications Security Rules API
  slug: postman-laravel-security-rules-api
- collection_type: postman
  name: Laravel Cloud Applications Server Credentials API
  slug: postman-laravel-server-credentials-api
- collection_type: postman
  name: Laravel Cloud Applications Servers API
  slug: postman-laravel-servers-api
- collection_type: postman
  name: Laravel Cloud Applications Sites API
  slug: postman-laravel-sites-api
- collection_type: postman
  name: Laravel Cloud Applications SSH Keys API
  slug: postman-laravel-ssh-keys-api
- collection_type: postman
  name: Laravel Cloud Applications Storage Providers API
  slug: postman-laravel-storage-providers-api
- collection_type: postman
  name: Laravel Cloud Applications Teams API
  slug: postman-laravel-teams-api
- collection_type: postman
  name: Laravel Cloud Applications Usage API
  slug: postman-laravel-usage-api
- collection_type: postman
  name: Laravel Cloud Applications User API
  slug: postman-laravel-user-api
- collection_type: postman
  name: Laravel Cloud Applications WebSocket Applications API
  slug: postman-laravel-websocket-applications-api
- collection_type: postman
  name: Laravel Cloud Applications WebSocket Clusters API
  slug: postman-laravel-websocket-clusters-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Laravel Cloud Applications API
  slug: open-laravel-applications-api
- collection_type: open
  name: Laravel Cloud Applications Background Processes API
  slug: open-laravel-background-processes-api
- collection_type: open
  name: Laravel Cloud Applications Backups API
  slug: open-laravel-backups-api
- collection_type: open
  name: Laravel Cloud Applications Bucket Keys API
  slug: open-laravel-bucket-keys-api
- collection_type: open
  name: Laravel Cloud Applications Caches API
  slug: open-laravel-caches-api
- collection_type: open
  name: Laravel Cloud Applications Commands API
  slug: open-laravel-commands-api
- collection_type: open
  name: Laravel Cloud Applications Database Clusters API
  slug: open-laravel-database-clusters-api
- collection_type: open
  name: Laravel Cloud Applications Database Restores API
  slug: open-laravel-database-restores-api
- collection_type: open
  name: Laravel Cloud Applications Database Snapshots API
  slug: open-laravel-database-snapshots-api
- collection_type: open
  name: Laravel Cloud Applications Databases API
  slug: open-laravel-databases-api
- collection_type: open
  name: Laravel Cloud Applications Databases (Legacy) API
  slug: open-laravel-databases-legacy-api
- collection_type: open
  name: Laravel Cloud Applications Dedicated Clusters API
  slug: open-laravel-dedicated-clusters-api
- collection_type: open
  name: Laravel Cloud Applications Deployments API
  slug: open-laravel-deployments-api
- collection_type: open
  name: Laravel Cloud Applications Domains API
  slug: open-laravel-domains-api
- collection_type: open
  name: Laravel Cloud Applications Environments API
  slug: open-laravel-environments-api
- collection_type: open
  name: Laravel Cloud Applications Firewall Rules API
  slug: open-laravel-firewall-rules-api
- collection_type: open
  name: Laravel Cloud Applications Instances API
  slug: open-laravel-instances-api
- collection_type: open
  name: Laravel Cloud Applications Integrations API
  slug: open-laravel-integrations-api
- collection_type: open
  name: Laravel Cloud Applications Logs API
  slug: open-laravel-logs-api
- collection_type: open
  name: Laravel Cloud Applications Meta API
  slug: open-laravel-meta-api
- collection_type: open
  name: Laravel Cloud Applications Monitors API
  slug: open-laravel-monitors-api
- collection_type: open
  name: Laravel Cloud Applications Nginx API
  slug: open-laravel-nginx-api
- collection_type: open
  name: Laravel Cloud Applications Object Storage Buckets API
  slug: open-laravel-object-storage-buckets-api
- collection_type: open
  name: Laravel Cloud Applications Organizations API
  slug: open-laravel-organizations-api
- collection_type: open
  name: Laravel Cloud Applications Providers API
  slug: open-laravel-providers-api
- collection_type: open
  name: Laravel Cloud Applications Recipes API
  slug: open-laravel-recipes-api
- collection_type: open
  name: Laravel Cloud Applications Redirect Rules API
  slug: open-laravel-redirect-rules-api
- collection_type: open
  name: Laravel Cloud Applications Roles API
  slug: open-laravel-roles-api
- collection_type: open
  name: Laravel Cloud Applications Scheduled Jobs API
  slug: open-laravel-scheduled-jobs-api
- collection_type: open
  name: Laravel Cloud Applications Security Rules API
  slug: open-laravel-security-rules-api
- collection_type: open
  name: Laravel Cloud Applications Server Credentials API
  slug: open-laravel-server-credentials-api
- collection_type: open
  name: Laravel Cloud Applications Servers API
  slug: open-laravel-servers-api
- collection_type: open
  name: Laravel Cloud Applications Sites API
  slug: open-laravel-sites-api
- collection_type: open
  name: Laravel Cloud Applications SSH Keys API
  slug: open-laravel-ssh-keys-api
- collection_type: open
  name: Laravel Cloud Applications Storage Providers API
  slug: open-laravel-storage-providers-api
- collection_type: open
  name: Laravel Cloud Applications Teams API
  slug: open-laravel-teams-api
- collection_type: open
  name: Laravel Cloud Applications Usage API
  slug: open-laravel-usage-api
- collection_type: open
  name: Laravel Cloud Applications User API
  slug: open-laravel-user-api
- collection_type: open
  name: Laravel Cloud Applications WebSocket Applications API
  slug: open-laravel-websocket-applications-api
- collection_type: open
  name: Laravel Cloud Applications WebSocket Clusters API
  slug: open-laravel-websocket-clusters-api
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/rate-limits/laravel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/laravel-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/plans/laravel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/laravel-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/capabilities/laravel-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/laravel-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/laravel/overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/security/laravel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/laravel-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/authentication/laravel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/laravel-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://laravel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://laravel.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://laravel.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://forge.laravel.com/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.laravel.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://laravel.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/laravel
- group: operate
  title: ''
  type: Support
  url: https://forge.laravel.com/docs/support
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/laravel
- group: commercial
  title: ''
  type: Pricing
  url: https://laravel.com/cloud/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.laravel.com/register
- group: start
  title: ''
  type: Login
  url: https://forge.laravel.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://laravel.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://laravel.com/legal/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/security/laravel-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/laravel-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.laravel.com/
- group: auth
  title: ''
  type: Security
  url: https://laravel.com/docs/13.x/contributions#security-vulnerabilities
- group: operate
  title: ''
  type: StatusPage
  url: https://status.laravel.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/lifecycle/laravel-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/laravel-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/lifecycle/laravel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/laravel-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/changelog/laravel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/laravel-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/packages/laravel-packages.yml
  title: ''
  type: Packages
  url: packages/laravel-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/packages/laravel-packages.yml
  title: ''
  type: SDKs
  url: packages/laravel-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/cli/laravel-cli.yml
  title: ''
  type: CLI
  url: cli/laravel-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/mcp/laravel-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/laravel-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/llms/laravel-forge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/laravel-forge-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/llms/laravel-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/laravel-cloud-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/security/laravel-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/laravel-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/overlays/laravel-forge-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/laravel-forge-overlay.yaml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/conventions/laravel-conventions.yml
  title: ''
  type: RateLimits
  url: conventions/laravel-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/well-known/laravel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/laravel-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/scopes/laravel-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/laravel-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/conventions/laravel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/laravel-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/errors/laravel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/laravel-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/conformance/laravel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/laravel-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/data-model/laravel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/laravel-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/asyncapi/laravel-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/laravel-webhooks.yml
created: '2026-07-17'
description: 'Laravel is the company behind the Laravel PHP framework and a suite of commercial developer infrastructure products: Laravel Cloud (a fully managed PaaS for deploying and scaling Laravel and Symfony applications), Laravel Forge (server provisioning and application deployment across DigitalOcean, AWS, Hetzner, Vultr, Akamai/Linode and custom VPS), Envoyer (zero-downtime PHP deployments), Vapor (serverless deployment on AWS Lambda), Nightwatch (application monitoring) and Nova (an administration panel). Both Laravel Cloud and the current Laravel Forge API publish machine-readable OpenAPI 3.1 descriptions and follow JSON:API-style conventions with cursor pagination, sparse filtering, sorting and relationship includes. Laravel also ships Laravel Boost, a first-party MCP server and Agent Skills bundle that gives AI coding agents structured access to Laravel ecosystem context and documentation.'
image: https://laravel.com/images/og/laravel-home.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 9 tools listed.
  name: Laravel MCP Server
  slug: laravel-boost
modified: '2026-07-19'
name: Laravel
nav: Providers
network: true
overview: 'Laravel publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Background Processes API, Backups API, and 39 more. Tagged areas include Company, Cloud Saas, PHP, Developer Tools, and Platform-as-a-Service.


  The Laravel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Laravel''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 37 more developer resources.'
plans:
- name: Laravel Plans Pricing
  plan_count: 11
  slug: laravel-plans-pricing
- name: Laravel Price Estimates
  plan_count: 0
  slug: laravel-price-estimates
random_paper: 17
rate_limits:
- limit_count: 1
  name: Laravel Rate Limits
  slug: laravel-rate-limits
scopes:
- name: Laravel Scopes
  scope_count: 62
  slug: laravel-scopes
  summary_line: 62 scopes · authorizationCode
score:
  band: exemplar
  composite: 69.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 61.3
    developer_ergonomics: 74.4
    discoverability: 73.2
    operational_transparency: 81.6
  previous_composite: 69.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/laravel/refs/heads/main/screenshots/laravel-2026-07-25T224538.png
security:
- kind: authentication
  name: Laravel Authentication
  slug: laravel-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Laravel Domain Security
  slug: laravel-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Laravel Vulnerability Disclosure
  slug: laravel-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Laravel Trust Center
  slug: laravel-trust-center
  summary_line: SOC 2 Type 2, HIPAA
slug: laravel
tags:
- Company
- Cloud Saas
- PHP
- Developer Tools
- Platform-as-a-Service
- Deployment
- Server Management
- Application Hosting
- Infrastructure
- Framework
- Monitoring
website: https://laravel.com/
---
