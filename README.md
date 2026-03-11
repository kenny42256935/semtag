1. SEMTAG BUILDING (EXAMPLE):
   
   run "SEMTAG3.py" with SEMTAG-003.xlsx on a local LLM
   
   output: "SEMTAG-3-001-output.csv
   
   compiled into "semtag-.csv" (the Tagset)

3. TAGGING Semtag to new data:
   
   run "TAGGING.py" with semtag-.csv and specify target file with "filename.txt"
   
   output: semtag-tagged data
   
   run "Count-tag-by text----.py" and specify target file with "filename-COUNT.txt"
   
   output: data for EFA

   "c-c-1-chienchien foodreview.txt"= sample text data
   
   "COUNT - EFA -JASP.jasp"= JASP result
   
