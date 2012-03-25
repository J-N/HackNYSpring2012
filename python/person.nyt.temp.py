  # Here until we can fix this. In the mean time, it's not that important
  # Semantic Person Database
  # Format is "lastname, firstname"
  # This will only work for people, rather than bands...
  # pages (inside of results) is the quantity we are interested in
  semanticData = ""
  whitespaces = re.findall("\s", artist)
  if len(whitespaces) == 1:
    tempName = ""
    person = ""
    match = re.search("\w*", artist)
    if match:
      tempName = match.group()
    else:
      print("Rut Roh")
      semanticData = "PROBLEM IN MATCHING!!! 1"
      data = [ articleData, semanticData ]
      return data
    match = re.search("\s\w*", artist)
    if match:
      person = match.group() + ", " + tempName
    else:
      print("Rut Roh")
      semanticData = "PROBLEM IN MATCHING!!! 2"
      data = [ articleData, semanticData ]
      return data
    semQuery = "West, Kanye" #person
    semQueryEncode = { "" : semQuery }
    semQueryData = urllib.urlencode(semQueryEncode)
    semAPIKey = APIKeys.getSemAPIKey()
    # From 1 to end, because we need to remove an = that the encode creates and requires
    nytSemanticUrl = "http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_per/" + semQueryData[1:] + ".json?&fields=pages&api-key=" + semAPIKey
    nytSemanticJSON = getRequest(nytSemanticUrl)
    # semantic sets the mode to look for the correct article fields
    # Output is a list full of strings
    print(nytSemanticJSON)
    semanticData = parseJSON.parseJSONnytimes(nytSemanticJSON, "semantic")
    #print(semanticData)
  else:
    data = 0