---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 74
  human_in_the_loop: 2
  name: Amazon Dms Agentic Access
  operation_count: 75
  slug: amazon-dms-agentic-access
  summary_line: 75 operations · 74 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://dms.amazonaws.com
  baseurl_source: declared
  description: Operations for managing source and target endpoints
  name: Amazon DMS Endpoints API
  slug: amazon-dms-endpoints-api
- baseURL: https://dms.amazonaws.com
  baseurl_source: declared
  description: Operations for managing DMS replication instances
  name: Amazon DMS Replication Instances API
  slug: amazon-dms-replication-instances-api
- baseURL: https://dms.amazonaws.com
  baseurl_source: declared
  description: Operations for managing replication tasks
  name: Amazon DMS Replication Tasks API
  slug: amazon-dms-replication-tasks-api
- baseURL: https://dms.amazonaws.com
  baseurl_source: declared
  description: The AWS Database Migration Service API from Amazon DMS — 69 operation(s) for aws database migration service.
  name: Amazon DMS AWS Database Migration Service API
  slug: amazon-dms-aws-database-migration-service-api
artifact_total: 247
collections:
- collection_type: postman
  name: AWS Database Migration Service Endpoints API
  slug: postman-amazon-dms-endpoints-api
- collection_type: postman
  name: AWS Database Migration Service Endpoints Replication Instances API
  slug: postman-amazon-dms-replication-instances-api
- collection_type: postman
  name: AWS Database Migration Service Endpoints Replication Tasks API
  slug: postman-amazon-dms-replication-tasks-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.AddTagsToResource API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-addtagstoresource-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ApplyPendingMaintenanceAction API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-applypendingmaintenanceaction-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.BatchStartRecommendations API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-batchstartrecommendations-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CancelReplicationTaskAssessmentRun API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-cancelreplicationtaskassessmentrun-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateEndpoint API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-createendpoint-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateEventSubscription API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-createeventsubscription-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateFleetAdvisorCollector API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-createfleetadvisorcollector-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateReplicationInstance API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-createreplicationinstance-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateReplicationSubnetGroup API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-createreplicationsubnetgroup-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateReplicationTask API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-createreplicationtask-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteCertificate API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deletecertificate-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteConnection API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deleteconnection-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteEndpoint API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deleteendpoint-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteEventSubscription API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deleteeventsubscription-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteFleetAdvisorCollector API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deletefleetadvisorcollector-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteFleetAdvisorDatabases API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deletefleetadvisordatabases-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteReplicationInstance API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deletereplicationinstance-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteReplicationSubnetGroup API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deletereplicationsubnetgroup-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteReplicationTask API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deletereplicationtask-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteReplicationTaskAssessmentRun API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-deletereplicationtaskassessmentrun-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeAccountAttributes API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeaccountattributes-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeApplicableIndividualAssessments API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeapplicableindividualassessments-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeCertificates API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describecertificates-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeConnections API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeconnections-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEndpoints API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeendpoints-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEndpointSettings API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeendpointsettings-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEndpointTypes API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeendpointtypes-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEventCategories API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeeventcategories-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEvents API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeevents-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEventSubscriptions API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeeventsubscriptions-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorCollectors API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisorcollectors-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorDatabases API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisordatabases-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorLsaAnalysis API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisorlsaanalysis-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorSchemaObjectSummary API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisorschemaobjectsummary-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorSchemas API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisorschemas-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeOrderableReplicationInstances API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeorderablereplicationinstances-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribePendingMaintenanceActions API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describependingmaintenanceactions-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeRecommendationLimitations API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describerecommendationlimitations-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeRecommendations API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describerecommendations-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeRefreshSchemasStatus API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describerefreshschemasstatus-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationInstances API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationinstances-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationInstanceTaskLogs API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationinstancetasklogs-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationSubnetGroups API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationsubnetgroups-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationTaskAssessmentResults API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationtaskassessmentresults-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationTaskAssessmentRuns API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationtaskassessmentruns-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationTaskIndividualAssessments API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationtaskindividualassessments-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationTasks API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationtasks-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeSchemas API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describeschemas-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeTableStatistics API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-describetablestatistics-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ImportCertificate API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-importcertificate-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ListTagsForResource API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-listtagsforresource-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyEndpoint API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-modifyendpoint-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyEventSubscription API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-modifyeventsubscription-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyReplicationInstance API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-modifyreplicationinstance-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyReplicationSubnetGroup API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-modifyreplicationsubnetgroup-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyReplicationTask API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-modifyreplicationtask-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.MoveReplicationTask API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-movereplicationtask-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.RebootReplicationInstance API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-rebootreplicationinstance-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.RefreshSchemas API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-refreshschemas-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ReloadTables API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-reloadtables-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.RemoveTagsFromResource API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-removetagsfromresource-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.RunFleetAdvisorLsaAnalysis API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-runfleetadvisorlsaanalysis-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StartRecommendations API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-startrecommendations-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StartReplicationTask API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-startreplicationtask-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StartReplicationTaskAssessment API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-startreplicationtaskassessment-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StartReplicationTaskAssessmentRun API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-startreplicationtaskassessmentrun-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StopReplicationTask API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-stopreplicationtask-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.TestConnection API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-testconnection-api
- collection_type: postman
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.UpdateSubscriptionsToEventBridge API'
  slug: postman-amazon-dms-x-amz-target-amazondmsv20160101-updatesubscriptionstoeventbridge-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Database Migration Service Endpoints API
  slug: open-amazon-dms-endpoints-api
- collection_type: open
  name: AWS Database Migration Service Endpoints Replication Instances API
  slug: open-amazon-dms-replication-instances-api
- collection_type: open
  name: AWS Database Migration Service Endpoints Replication Tasks API
  slug: open-amazon-dms-replication-tasks-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.AddTagsToResource API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-addtagstoresource-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ApplyPendingMaintenanceAction API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-applypendingmaintenanceaction-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.BatchStartRecommendations API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-batchstartrecommendations-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CancelReplicationTaskAssessmentRun API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-cancelreplicationtaskassessmentrun-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateEndpoint API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-createendpoint-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateEventSubscription API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-createeventsubscription-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateFleetAdvisorCollector API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-createfleetadvisorcollector-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateReplicationInstance API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-createreplicationinstance-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateReplicationSubnetGroup API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-createreplicationsubnetgroup-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.CreateReplicationTask API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-createreplicationtask-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteCertificate API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deletecertificate-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteConnection API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deleteconnection-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteEndpoint API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deleteendpoint-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteEventSubscription API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deleteeventsubscription-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteFleetAdvisorCollector API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deletefleetadvisorcollector-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteFleetAdvisorDatabases API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deletefleetadvisordatabases-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteReplicationInstance API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deletereplicationinstance-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteReplicationSubnetGroup API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deletereplicationsubnetgroup-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteReplicationTask API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deletereplicationtask-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DeleteReplicationTaskAssessmentRun API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-deletereplicationtaskassessmentrun-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeAccountAttributes API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeaccountattributes-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeApplicableIndividualAssessments API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeapplicableindividualassessments-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeCertificates API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describecertificates-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeConnections API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeconnections-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEndpoints API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeendpoints-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEndpointSettings API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeendpointsettings-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEndpointTypes API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeendpointtypes-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEventCategories API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeeventcategories-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEvents API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeevents-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeEventSubscriptions API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeeventsubscriptions-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorCollectors API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisorcollectors-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorDatabases API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisordatabases-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorLsaAnalysis API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisorlsaanalysis-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorSchemaObjectSummary API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisorschemaobjectsummary-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeFleetAdvisorSchemas API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describefleetadvisorschemas-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeOrderableReplicationInstances API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeorderablereplicationinstances-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribePendingMaintenanceActions API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describependingmaintenanceactions-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeRecommendationLimitations API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describerecommendationlimitations-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeRecommendations API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describerecommendations-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeRefreshSchemasStatus API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describerefreshschemasstatus-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationInstances API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationinstances-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationInstanceTaskLogs API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationinstancetasklogs-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationSubnetGroups API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationsubnetgroups-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationTaskAssessmentResults API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationtaskassessmentresults-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationTaskAssessmentRuns API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationtaskassessmentruns-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationTaskIndividualAssessments API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationtaskindividualassessments-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeReplicationTasks API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describereplicationtasks-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeSchemas API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describeschemas-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.DescribeTableStatistics API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-describetablestatistics-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ImportCertificate API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-importcertificate-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ListTagsForResource API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-listtagsforresource-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyEndpoint API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-modifyendpoint-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyEventSubscription API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-modifyeventsubscription-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyReplicationInstance API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-modifyreplicationinstance-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyReplicationSubnetGroup API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-modifyreplicationsubnetgroup-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ModifyReplicationTask API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-modifyreplicationtask-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.MoveReplicationTask API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-movereplicationtask-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.RebootReplicationInstance API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-rebootreplicationinstance-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.RefreshSchemas API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-refreshschemas-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.ReloadTables API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-reloadtables-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.RemoveTagsFromResource API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-removetagsfromresource-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.RunFleetAdvisorLsaAnalysis API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-runfleetadvisorlsaanalysis-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StartRecommendations API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-startrecommendations-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StartReplicationTask API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-startreplicationtask-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StartReplicationTaskAssessment API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-startreplicationtaskassessment-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StartReplicationTaskAssessmentRun API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-startreplicationtaskassessmentrun-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.StopReplicationTask API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-stopreplicationtask-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.TestConnection API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-testconnection-api
- collection_type: open
  name: 'AWS Database Migration Service Endpoints #X Amz Target=AmazonDMSv20160101.UpdateSubscriptionsToEventBridge API'
  slug: open-amazon-dms-x-amz-target-amazondmsv20160101-updatesubscriptionstoeventbridge-api
- collection_type: open
  name: Amazon DMS AWS Database Migration Service API
  slug: open-amazon-dms
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/pricing/?nc2=h_pr_hub
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/plans/amazon-dms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-dms-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/capabilities/amazon-dms-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-dms-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-dms/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/agentic-access/amazon-dms-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-dms-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/security/amazon-dms-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-dms-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/security/amazon-dms-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-dms-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/security/amazon-dms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-dms-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/authentication/amazon-dms-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-dms-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/dms/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/dms/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/dms/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/database/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/dms/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/rules/amazon-dms-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/vocabulary/amazon-dms-vocabulary.yaml
created: '2024-01-15'
description: AWS Database Migration Service (AWS DMS) helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. AWS DMS can migrate your data to and from the most widely used commercial and open-source databases, supporting homogeneous and heterogeneous migrations with continuous data replication.
examples:
- key_count: 3
  name: Amazon Dms Account Quota Example
  slug: amazon-dms-account-quota-example
- key_count: 1
  name: Amazon Dms Availability Zone Example
  slug: amazon-dms-availability-zone-example
- key_count: 10
  name: Amazon Dms Certificate Example
  slug: amazon-dms-certificate-example
- key_count: 13
  name: Amazon Dms Collector Response Example
  slug: amazon-dms-collector-response-example
- key_count: 6
  name: Amazon Dms Connection Example
  slug: amazon-dms-connection-example
- key_count: 7
  name: Amazon Dms Database Response Example
  slug: amazon-dms-database-response-example
- key_count: 35
  name: Amazon Dms Endpoint Example
  slug: amazon-dms-endpoint-example
- key_count: 9
  name: Amazon Dms Event Subscription Example
  slug: amazon-dms-event-subscription-example
- key_count: 6
  name: Amazon Dms Limitation Example
  slug: amazon-dms-limitation-example
- key_count: 9
  name: Amazon Dms Orderable Replication Instance Example
  slug: amazon-dms-orderable-replication-instance-example
- key_count: 6
  name: Amazon Dms Pending Maintenance Action Example
  slug: amazon-dms-pending-maintenance-action-example
- key_count: 5
  name: Amazon Dms Refresh Schemas Status Example
  slug: amazon-dms-refresh-schemas-status-example
- key_count: 25
  name: Amazon Dms Replication Instance Example
  slug: amazon-dms-replication-instance-example
- key_count: 3
  name: Amazon Dms Replication Instance Task Log Example
  slug: amazon-dms-replication-instance-task-log-example
- key_count: 6
  name: Amazon Dms Replication Subnet Group Example
  slug: amazon-dms-replication-subnet-group-example
- key_count: 7
  name: Amazon Dms Replication Task Assessment Result Example
  slug: amazon-dms-replication-task-assessment-result-example
- key_count: 12
  name: Amazon Dms Replication Task Assessment Run Example
  slug: amazon-dms-replication-task-assessment-run-example
- key_count: 19
  name: Amazon Dms Replication Task Example
  slug: amazon-dms-replication-task-example
- key_count: 11
  name: Amazon Dms Replication Task Stats Example
  slug: amazon-dms-replication-task-stats-example
- key_count: 9
  name: Amazon Dms Schema Response Example
  slug: amazon-dms-schema-response-example
- key_count: 3
  name: Amazon Dms Subnet Example
  slug: amazon-dms-subnet-example
- key_count: 5
  name: Amazon Dms Supported Endpoint Type Example
  slug: amazon-dms-supported-endpoint-type-example
- key_count: 23
  name: Amazon Dms Table Statistics Example
  slug: amazon-dms-table-statistics-example
- key_count: 3
  name: Amazon Dms Tag Example
  slug: amazon-dms-tag-example
- key_count: 2
  name: Amazon Dms Vpc Security Group Membership Example
  slug: amazon-dms-vpc-security-group-membership-example
features:
- description: Migrate between databases of the same engine type with minimal conversion
  name: Homogeneous Migration
- description: Migrate between different database engines using Schema Conversion Tool
  name: Heterogeneous Migration
- description: Continuously replicate data changes using change data capture (CDC)
  name: Continuous Data Replication
- description: Keep source database operational during migration for high availability
  name: Minimal Downtime Migration
- description: Provision replication instances across multiple Availability Zones for resilience
  name: Multi-AZ Replication
- description: Run automated assessments to identify migration issues before starting
  name: Premigration Assessment
finops:
- name: Amazon Dms Finops
  service_category: API
  slug: amazon-dms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-dms.png
json_schemas:
- name: AccountQuota
  property_count: 3
  slug: amazon-dms-account-quota
- name: AvailabilityZone
  property_count: 1
  slug: amazon-dms-availability-zone
- name: Certificate
  property_count: 10
  slug: amazon-dms-certificate
- name: CollectorResponse
  property_count: 13
  slug: amazon-dms-collector-response
- name: Connection
  property_count: 6
  slug: amazon-dms-connection
- name: DatabaseResponse
  property_count: 7
  slug: amazon-dms-database-response
- name: Endpoint
  property_count: 35
  slug: amazon-dms-endpoint
- name: EventSubscription
  property_count: 9
  slug: amazon-dms-event-subscription
- name: Limitation
  property_count: 6
  slug: amazon-dms-limitation
- name: OrderableReplicationInstance
  property_count: 9
  slug: amazon-dms-orderable-replication-instance
- name: PendingMaintenanceAction
  property_count: 6
  slug: amazon-dms-pending-maintenance-action
- name: RefreshSchemasStatus
  property_count: 5
  slug: amazon-dms-refresh-schemas-status
- name: ReplicationInstance
  property_count: 25
  slug: amazon-dms-replication-instance
- name: ReplicationInstanceTaskLog
  property_count: 3
  slug: amazon-dms-replication-instance-task-log
- name: ReplicationSubnetGroup
  property_count: 6
  slug: amazon-dms-replication-subnet-group
- name: ReplicationTaskAssessmentResult
  property_count: 7
  slug: amazon-dms-replication-task-assessment-result
- name: ReplicationTaskAssessmentRun
  property_count: 12
  slug: amazon-dms-replication-task-assessment-run
- name: ReplicationTask
  property_count: 19
  slug: amazon-dms-replication-task
- name: ReplicationTaskStats
  property_count: 11
  slug: amazon-dms-replication-task-stats
- name: SchemaResponse
  property_count: 9
  slug: amazon-dms-schema-response
- name: Subnet
  property_count: 3
  slug: amazon-dms-subnet
- name: SupportedEndpointType
  property_count: 5
  slug: amazon-dms-supported-endpoint-type
- name: TableStatistics
  property_count: 23
  slug: amazon-dms-table-statistics
- name: Tag
  property_count: 3
  slug: amazon-dms-tag
- name: VpcSecurityGroupMembership
  property_count: 2
  slug: amazon-dms-vpc-security-group-membership
json_structures:
- name: Amazon Dms Account Quota Structure
  property_count: 3
  slug: amazon-dms-account-quota-structure
- name: Amazon Dms Availability Zone Structure
  property_count: 1
  slug: amazon-dms-availability-zone-structure
- name: Amazon Dms Certificate Structure
  property_count: 10
  slug: amazon-dms-certificate-structure
- name: Amazon Dms Collector Response Structure
  property_count: 13
  slug: amazon-dms-collector-response-structure
- name: Amazon Dms Connection Structure
  property_count: 6
  slug: amazon-dms-connection-structure
- name: Amazon Dms Database Response Structure
  property_count: 7
  slug: amazon-dms-database-response-structure
- name: Amazon Dms Endpoint Structure
  property_count: 35
  slug: amazon-dms-endpoint-structure
- name: Amazon Dms Event Subscription Structure
  property_count: 9
  slug: amazon-dms-event-subscription-structure
- name: Amazon Dms Limitation Structure
  property_count: 6
  slug: amazon-dms-limitation-structure
- name: Amazon Dms Orderable Replication Instance Structure
  property_count: 9
  slug: amazon-dms-orderable-replication-instance-structure
- name: Amazon Dms Pending Maintenance Action Structure
  property_count: 6
  slug: amazon-dms-pending-maintenance-action-structure
- name: Amazon Dms Refresh Schemas Status Structure
  property_count: 5
  slug: amazon-dms-refresh-schemas-status-structure
- name: Amazon Dms Replication Instance Structure
  property_count: 25
  slug: amazon-dms-replication-instance-structure
- name: Amazon Dms Replication Instance Task Log Structure
  property_count: 3
  slug: amazon-dms-replication-instance-task-log-structure
- name: Amazon Dms Replication Subnet Group Structure
  property_count: 6
  slug: amazon-dms-replication-subnet-group-structure
- name: Amazon Dms Replication Task Assessment Result Structure
  property_count: 7
  slug: amazon-dms-replication-task-assessment-result-structure
- name: Amazon Dms Replication Task Assessment Run Structure
  property_count: 12
  slug: amazon-dms-replication-task-assessment-run-structure
- name: Amazon Dms Replication Task Stats Structure
  property_count: 11
  slug: amazon-dms-replication-task-stats-structure
- name: Amazon Dms Replication Task Structure
  property_count: 19
  slug: amazon-dms-replication-task-structure
- name: Amazon Dms Schema Response Structure
  property_count: 9
  slug: amazon-dms-schema-response-structure
- name: Amazon Dms Subnet Structure
  property_count: 3
  slug: amazon-dms-subnet-structure
- name: Amazon Dms Supported Endpoint Type Structure
  property_count: 5
  slug: amazon-dms-supported-endpoint-type-structure
- name: Amazon Dms Table Statistics Structure
  property_count: 23
  slug: amazon-dms-table-statistics-structure
- name: Amazon Dms Tag Structure
  property_count: 3
  slug: amazon-dms-tag-structure
- name: Amazon Dms Vpc Security Group Membership Structure
  property_count: 2
  slug: amazon-dms-vpc-security-group-membership-structure
jsonld:
- class_count: 25
  name: Amazon Dms Context
  property_count: 198
  slug: amazon-dms-context
layout: provider
modified: '2026-05-19'
name: Amazon DMS
nav: Providers
network: true
overview: 'Amazon DMS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Endpoints API, Replication Instances API, Replication Tasks API, and 1 more. Tagged areas include Data Replication, Database, Database Migration, and Migration.


  The Amazon DMS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon DMS''s developer surface includes pricing, authentication, developer portal, documentation, support, engineering blog, developer console, and 17 more developer resources.'
plans:
- name: Amazon Dms Plans Pricing
  plan_count: 0
  slug: amazon-dms-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Amazon Dms Rate Limits
  slug: amazon-dms-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon DMS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-dms-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Amazon DMS API Rules
  rule_count: 23
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 9
  slug: amazon-dms-spectral-rules
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 53.9
    contract_governance: 27.3
    contract_quality: 55.7
    developer_ergonomics: 51.2
    discoverability: 57.1
    operational_transparency: 26.3
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 25.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/screenshots/amazon-dms-2026-06-20T171625.png
security:
- kind: authentication
  name: Amazon Dms Authentication
  slug: amazon-dms-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Dms Domain Security
  slug: amazon-dms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Dms Vulnerability Disclosure
  slug: amazon-dms-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Dms Trust Center
  slug: amazon-dms-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-dms
tags:
- Data Replication
- Database
- Database Migration
- Migration
use_cases:
- description: Consolidate multiple databases into a single AWS-managed database
  name: Database Consolidation
- description: Migrate from Oracle or SQL Server to open-source Aurora or PostgreSQL
  name: Cross-Engine Migration
- description: Continuously replicate production data to development environments
  name: Development and Testing
- description: Maintain synchronized database replicas across regions for failover
  name: Active-Active Replication
- description: Migrate transactional databases to analytical data warehouses like Redshift
  name: Analytics Migration
website: https://aws.amazon.com/dms/
---
