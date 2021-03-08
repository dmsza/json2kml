<?xml version="1.0" encoding="UTF-8"?>
<kml
  xmlns="http://www.opengis.net/kml/2.2"
  xmlns:gx="http://www.google.com/kml/ext/2.2">
  <Document id="10">
      <name>${path|x}</name>
      % for p in places:
      <Placemark id="${loop.index + 2000}">
          <name>${p.name|x}</name>
          <description>
          <![CDATA[
            ${p.note}
            ${p.comment}
            <a href="${p.url}">${p.url}</a>
          ]]>
          </description>
          <address>${p.address|x}</address>
          <Point id="${loop.index + 1000}">
          <coordinates>${f'{p.long:0.6f},{p.lat:0.6f},0.0'}</coordinates>
          </Point>
      </Placemark>
      % endfor
  </Document>
</kml>
