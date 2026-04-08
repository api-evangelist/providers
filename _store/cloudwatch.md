---
aid: cloudwatch
url: https://raw.githubusercontent.com/api-evangelist/cloudwatch/refs/heads/main/apis.yml
apis:
- name: Amazon CloudWatch API
  description: Core CloudWatch API for metrics, alarms, and dashboards.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudwatch/
  baseURL: https://monitoring.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cloudwatch/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/monitoring/2010-08-01/openapi.yaml
  - type: OpenAPI
    url: openapi/cloudwatch-openapi.yml
  - type: JSON Schema
    url: json-schema/cloudwatch-alarm-schema.json
  - type: JSON Schema
    url: json-schema/cloudwatch-metric-schema.json
  - type: JSON-LD Context
    url: json-ld/cloudwatch-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/cloudwatch/pricing/
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingStarted.html
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/
  - type: Console
    url: https://console.aws.amazon.com/cloudwatch/
  - type: Features
    url: https://aws.amazon.com/cloudwatch/features/
  tags:
  - Alarms
  - Dashboards
  - Metric-Streams
  - Metrics
  - Statistics
- name: Amazon CloudWatch Logs API
  description: API for ingesting, storing, and analyzing log data.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudwatch/features/
  baseURL: https://logs.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/logs/2014-03-28/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/
  - type: Query Syntax
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html
  - type: Logs Insights
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html
  - type: SDK
    url: https://aws.amazon.com/tools/
  tags:
  - Insights
  - Log-Analytics
  - Log-Groups
  - Log-Streams
  - Logs
- name: Amazon CloudWatch Events API
  description: Event-driven architecture for responding to state changes in AWS resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/eventbridge/
  baseURL: https://events.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/eventbridge/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/events/2015-10-07/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/
  - type: SDK
    url: https://aws.amazon.com/tools/
  tags:
  - Event-Bus
  - Eventbridge
  - Events
  - Rules
  - Targets
- name: Amazon CloudWatch Application Insights API
  description: Automated monitoring for applications with anomaly detection.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudwatch/features/
  baseURL: https://applicationinsights.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/application-insights/2018-11-25/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/
  - type: SDK
    url: https://aws.amazon.com/tools/
  tags:
  - Anomaly-Detection
  - Application-Insights
  - Observability
- name: Amazon CloudWatch Synthetics API
  description: API for creating and managing canaries that continuously monitor endpoints and APIs using synthetic traffic.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html
  baseURL: https://synthetics.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/synthetics/2017-10-11/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/
  - type: SDK
    url: https://aws.amazon.com/tools/
  tags:
  - Canaries
  - Endpoint-Monitoring
  - Monitoring
  - Synthetics
- name: Amazon CloudWatch Internet Monitor API
  description: API for monitoring internet performance and availability between applications hosted on AWS and end users.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html
  baseURL: https://internetmonitor.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/internetmonitor/2021-06-03/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/internet-monitor/latest/api/Welcome.html
  - type: SDK
    url: https://aws.amazon.com/tools/
  tags:
  - Availability
  - Internet-Monitor
  - Latency
  - Network-Performance
- name: Amazon CloudWatch RUM API
  description: API for real user monitoring to collect client-side data about web and mobile application performance from actual user sessions.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html
  baseURL: https://rum.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/rum/2018-05-10/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/Welcome.html
  - type: SDK
    url: https://aws.amazon.com/tools/
  tags:
  - Client-Side
  - Real-User-Monitoring
  - Rum
  - Web-Performance
- name: Amazon CloudWatch Observability Access Manager API
  description: API for creating and managing cross-account observability links between source accounts and monitoring accounts.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html
  baseURL: https://oam.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/oam/2022-06-10/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/OAM/latest/APIReference/Welcome.html
  - type: SDK
    url: https://aws.amazon.com/tools/
  tags:
  - Cross-Account
  - Monitoring-Account
  - Oam
  - Observability
- name: Amazon CloudWatch Application Signals API
  description: API for automatic instrumentation and monitoring of application services with service level objectives.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudwatch/features/application-observability-apm/
  baseURL: https://application-signals.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html
  - type: API Reference
    url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/Welcome.html
  - type: SDK
    url: https://aws.amazon.com/tools/
  tags:
  - Apm
  - Application-Signals
  - Service-Level-Objectives
  - Slo
- name: Amazon CloudWatch Network Monitor API
  description: API for active network monitoring to identify network issues within AWS or company networks using synthetic probes.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudwatch/features/network-monitoring/
  baseURL: https://networkmonitor.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html
  - type: API Reference
    url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html
  - type: SDK
    url: https://aws.amazon.com/tools/
  tags:
  - Direct-Connect
  - Hybrid-Connectivity
  - Network-Monitor
  - Network-Performance
name: AWS CloudWatch
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights for AWS, hybrid, and on-premises applications and infrastructure resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

