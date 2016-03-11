<?php


Yii::$app->db_mssql->createCommand("SET ANSI_NULLS ON")->execute();
Yii::$app->db_mssql->createCommand("SET  ANSI_WARNINGS ON")->execute();
//necesitamos las 2 lineas anteriores para poder ejecutar una consulta o store procedure con consultas heterogeneas
$lista = Yii::$app->db_mssql->createCommand("SELECT *FROM openquery(DB_MYSQL,'select *from archivo')")->queryAll();
?>
