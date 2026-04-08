---
aid: hadoop
url: https://raw.githubusercontent.com/api-evangelist/hadoop/refs/heads/main/apis.yml
apis:
- aid: hadoop:hdfs-rest-api
  name: HDFS REST API (WebHDFS)
  description: RESTful API for Hadoop Distributed File System operations including file operations, directory operations, and file status queries.
  humanURL: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/WebHDFS.html
  baseURL: http://host:port/webhdfs/v1/
  tags:
  - File System
  - REST API
  - Storage
  properties:
  - type: Documentation
    url: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/WebHDFS.html
- aid: hadoop:yarn-rest-api
  name: YARN REST API
  description: RESTful API for Yet Another Resource Negotiator (YARN) for cluster resource management, application submission, and monitoring.
  humanURL: https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html
  baseURL: http://rm-http-address:port/ws/v1/
  tags:
  - Cluster Management
  - Resource Management
  - REST API
  properties:
  - type: Documentation
    url: https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html
- aid: hadoop:mapreduce-history-server-api
  name: MapReduce History Server REST API
  description: REST API for accessing MapReduce job history and statistics.
  humanURL: https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapredAppMasterRest.html
  tags:
  - Job History
  - MapReduce
  - REST API
  properties:
  - type: Documentation
    url: https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapredAppMasterRest.html
- aid: hadoop:httpfs-rest-api
  name: HttpFS REST API
  description: HTTP REST API gateway supporting both webhdfs and httpfs operations for HDFS access.
  humanURL: https://hadoop.apache.org/docs/stable/hadoop-hdfs-httpfs/index.html
  baseURL: http://httpfs-host:port/webhdfs/v1/
  tags:
  - File System
  - Gateway
  - REST API
  properties:
  - type: Documentation
    url: https://hadoop.apache.org/docs/stable/hadoop-hdfs-httpfs/index.html
name: Apache Hadoop
tags:
- Big Data
- Data Processing
- Distributed Computing
- HDFS
- MapReduce
- Open Source
type: Contract
image: https://hadoop.apache.org/hadoop-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache Hadoop is an open-source framework for distributed storage and processing of large datasets across clusters of computers using simple programming models. It includes HDFS for distributed storage, YARN for resource management, and MapReduce for parallel data processing.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

