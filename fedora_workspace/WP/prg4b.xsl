<?xml version="1.0" encoding="utf-8"?> 
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns="http://www.w3.org.org/1999/xhtml"> 
<xsl:template match="student_information"> 
<html><head><title>program4b.xsl</title> 
</head><body> 
<span style="font-size:20pt;font-weight:bold;color:red;">USN:</span> 
<xsl:value-of select="ad/usn"/> <br/> 
<span style="font-size:20pt;font-weight:bold;color:red;">NAME:</span> 
<xsl:value-of select="ad/name"/><br/>  
<span style="font-size:20pt;font-weight:bold;color:red;">COLLEGE:</span> 
<xsl:value-of select="ad/college"/><br/>  
<span style="font-size:20pt;font-weight:bold;color:red;">BRANCH:</span> 
<xsl:value-of select="ad/branch"/><br/>  
<span style="font-size:20pt;font-weight:bold;color:red;">YEAR:</span> 
<xsl:value-of select="ad/year"/><br/>  
<span style="font-size:20pt;font-weight:bold;color:red;">EMAIL:</span> 
<xsl:value-of select="ad/email"/><br/>  
</body></html> 
</xsl:template> 
</xsl:stylesheet> 



