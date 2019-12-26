
CREATE TABLE IF NOT EXISTS User.ex_online_user
(
    uid             int    COMMENT '用户id              '
   ,ostype          int    COMMENT '当日最后一次登录设备'    
)
partitioned by (
    pt_dt    string,
    dt       string
)
STORED AS PARQUET;


INSERT OVERWRITE TABLE User.ex_online_user partition(pt_dt='${hivevar:OP_DATE}',dt='${hivevar:OP_DATE}')
select uid,ostype  
from (   
    select uid,tostype ostype ,row_number() over (partition by uid order by logindt desc) as rn 
    from dwd.dwd_usr_online_d 
    where pt_dt = '${hivevar:OP_DATE}'
) T1 
where rn=1 ;

