import{useEffect,useMemo,useState}from"react";import{getFinancials,getBalanceSheet,getCashFlow,getDividends}from"../api/client";
import type { DataRecord } from "../api/client";import{LineChart}from"../components/Charts";import Panel from"../components/Panel";
import RecordTable from"../components/RecordTable";type Tab="income"|"balance"|"cashflow"|"dividends";const date=(r:DataRecord)=>String(r.date??r.Date??"");
export default function Financials(){const[symbol,setSymbol]=useState("AAPL"),[tab,setTab]=useState<Tab>("income"),[rows,setRows]=useState<DataRecord[]>([]),[selected,setSelected]=useState(""),[err,setErr]=useState("");useEffect(()=>{const p=tab==="income"?getFinancials(symbol):tab==="balance"?getBalanceSheet(symbol):tab==="cashflow"?getCashFlow(symbol):getDividends(symbol);p.then(x=>{setRows(x);setSelected(date(x.at(-1)??{}))}).catch(e=>setErr(e.message))},[symbol,tab]);const dates=useMemo(()=>rows.map(date).filter(Boolean),[rows]);const row=rows.find(x=>date(x)===selected)??rows.at(-1);const numeric=(row?Object.entries(row):[]).filter(([k,v])=>k!=="date"&&k!=="Date"&&typeof v==="number");
const dividend = tab === "dividends"
    ? (() => {
        const dividendMap = new Map<string, number>();

        rows.forEach(r => {
            const time = date(r);
            const value = Number(r.value ?? 0);

            if (time && Number.isFinite(value)) {
                dividendMap.set(
                    time,
                    (dividendMap.get(time) ?? 0) + value
                );
            }
        });

        return Array.from(dividendMap.entries())
            .map(([time, value]) => ({
                time,
                value
            }))
            .sort((a, b) => a.time.localeCompare(b.time));
    })()
    : [];
const tabs:[Tab,string][]=[["income","Income Statement"],["balance","Balance Sheet"],["cashflow","Cash Flow"],["dividends","Dividends"]];
return <><div className="heading"><div><span>COMPANY FINANCIALS</span><h1>{symbol}</h1><p>Financial data from FastAPI.</p></div><input className="ticker" value={symbol} onChange={e=>setSymbol(e.target.value.toUpperCase())}/></div><div className="tabs">{tabs.map(([v,l])=><button className={tab===v?"active":""} onClick={()=>setTab(v)} key={v}>{l}</button>)}</div>{err&&<div className="error">{err}</div>}<Panel title={tabs.find(x=>x[0]===tab)?.[1]??""} subtitle={`${rows.length} records`} actions={tab!=="dividends"&&<select value={selected} onChange={e=>setSelected(e.target.value)}>{dates.map(d=><option key={d}>{d}</option>)}</select>}>{tab==="dividends"?<><LineChart data={dividend}/><RecordTable rows={rows}/></>:<div className="financials">{numeric.map(([k,v])=><div key={k}><small>{k}</small><b>{Number(v).toLocaleString(undefined,{maximumFractionDigits:4})}</b></div>)}</div>}</Panel></>}