<template>
    <div class="title">
      <h3> View3 - Tweets grouped by genres </h3>
    </div>
    <div>
        <ul></ul>
        <div ref="chart" style="height: 500px;"></div>
        <ul>{{string}}</ul>
    </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
    name: 'FirstView',
    props: {
        msg: String
    },
    data() {
        return {
            string: 'Sports genre by cities',
            chart: null,
            chartData: []
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://172.26.133.58:5000/genre');
                console.log(response.data);
                this.chartData = response.data;
                this.updateChart();
            } catch (error) {
                console.log(error);
            }
        },
        updateChart() {
            this.chart.setOption(
                {
                  legend: {},
                  tooltip: {},
                  dataset: {
                    source: this.chartData
                  },
                  title: [
                    {
                      subtext: 'Sydney',
                      left: '25%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: 'Melbourne',
                      left: '75%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: 'Brisbane',
                      left: '25%',
                      top: '90%',
                      textAlign: 'center'
                    }
                  ],
                  series: [
                    {
                      type: 'pie',
                      radius: '20%',
                      center: ['25%', '30%']
                      // No encode specified, by default, it is '2012'.
                    },
                    {
                      type: 'pie',
                      radius: '20%',
                      center: ['75%', '30%'],
                      encode: {
                        itemName: '',
                        value: '2gmel'
                      }
                    },
                    {
                      type: 'pie',
                      radius: '20%',
                      center: ['25%', '75%'],
                      encode: {
                        itemName: '',
                        value: '3gbri'
                      }
                    }
                  ]
                }
            );
        },
    },
    mounted() {
        this.chart = echarts.init(this.$refs.chart);
        this.getData1();
    },
}
</script>

<style lang="scss" scoped>
.title {
  margin-top: 40px;
}
</style>