<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.2" tiledversion="1.2.4" name="tiles" tilewidth="15" tileheight="15" tilecount="100" columns="10">
 <image source="tiles.png" width="150" height="150"/>
 <tile id="0">
  <properties>
   <property name="Goal" type="bool" value="true"/>
   <property name="Slow" type="bool" value="false"/>
   <property name="Wall" type="bool" value="false"/>
  </properties>
 </tile>
 <tile id="1">
  <properties>
   <property name="Slow" type="bool" value="false"/>
   <property name="Wall" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="2">
  <properties>
   <property name="Slow" type="bool" value="true"/>
   <property name="Wall" type="bool" value="false"/>
  </properties>
 </tile>
 <tile id="3">
  <properties>
   <property name="Slow" type="bool" value="false"/>
   <property name="Wall" type="bool" value="false"/>
  </properties>
 </tile>
</tileset>
